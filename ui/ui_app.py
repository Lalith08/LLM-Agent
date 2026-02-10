import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from agent import agent, message_history
from datetime import datetime
import json

st.set_page_config(
    page_title="LLM Agent Assistant",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

if "messages" not in st.session_state:
    st.session_state.messages = []

if "show_agent_thoughts" not in st.session_state:
    st.session_state.show_agent_thoughts = False

with st.sidebar:
    st.title("⚙️ Settings")
    
    st.markdown("---")
    st.subheader("💬 Chat Controls")
    
    if st.button("🗑️ Clear Chat History", use_container_width=True):
        st.session_state.messages = []
        message_history.clear()
        st.rerun()
    
    if st.button("📥 Export Chat", use_container_width=True):
        if st.session_state.messages:
            chat_export = {
                "exported_at": datetime.now().isoformat(),
                "messages": st.session_state.messages
            }
            st.download_button(
                label="Download JSON",
                data=json.dumps(chat_export, indent=2),
                file_name=f"chat_export_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
                mime="application/json",
                use_container_width=True
            )
        else:
            st.info("No messages to export")
    
    st.markdown("---")
    st.subheader("🔧 Display Options")
    
    st.session_state.show_agent_thoughts = st.checkbox(
        "Show Agent Reasoning",
        value=st.session_state.show_agent_thoughts,
        help="Display the agent's step-by-step thinking process"
    )
    
    st.markdown("---")
    st.subheader("🛠️ Available Tools")
    st.markdown("""
    - **Calculator**: Math expressions
    - **Code Executor**: Python code (sandboxed)
    - **Web Search**: DuckDuckGo search
    - **PDF Summarizer**: Summarize PDFs
    """)
    
    st.markdown("---")
    st.subheader("💡 Example Queries")
    
    examples = [
        "Calculate sqrt(144) + 2**8",
        "Search for latest AI breakthroughs",
        "Execute: print([x**2 for x in range(10)])",
        "Summarize pdfs/sample.pdf"
    ]
    
    for example in examples:
        if st.button(f"📝 {example[:30]}...", key=example, use_container_width=True):
            st.session_state.example_query = example

st.title("🤖 LLM Agent Assistant")
st.markdown("*Powered by GPT-4o-mini with LangChain*")

st.markdown("---")

for idx, message in enumerate(st.session_state.messages):
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        
        if message["role"] == "assistant" and "timestamp" in message:
            st.caption(f"🕒 {message['timestamp']}")
        
        if message["role"] == "assistant" and "thoughts" in message and st.session_state.show_agent_thoughts:
            with st.expander("🧠 Agent Reasoning"):
                st.text(message["thoughts"])

if hasattr(st.session_state, 'example_query'):
    prompt = st.session_state.example_query
    del st.session_state.example_query
else:
    prompt = st.chat_input("Ask me anything... (e.g., 'Calculate 15 * 23', 'Search for Python tutorials')")

if prompt:
    st.session_state.messages.append({
        "role": "user",
        "content": prompt,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })
    
    with st.chat_message("user"):
        st.markdown(prompt)
    
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        thoughts_placeholder = st.empty()
        
        try:
            with st.spinner("🤔 Thinking..."):
                import io
                from contextlib import redirect_stdout
                
                thoughts_buffer = io.StringIO()
                
                with redirect_stdout(thoughts_buffer):
                    response = agent.run(prompt)
                
                agent_thoughts = thoughts_buffer.getvalue()
                
                if not response:
                    response = "❌ I couldn't generate a response. Please try again."
                
                message_placeholder.markdown(response)
                
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                st.caption(f"🕒 {timestamp}")
                
                if agent_thoughts and st.session_state.show_agent_thoughts:
                    with st.expander("🧠 Agent Reasoning"):
                        st.text(agent_thoughts)
                
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": response,
                    "timestamp": timestamp,
                    "thoughts": agent_thoughts
                })
                
        except Exception as e:
            error_message = f"❌ **Error**: {str(e)}\n\nPlease try rephrasing your question or check the logs."
            message_placeholder.markdown(error_message)
            
            st.session_state.messages.append({
                "role": "assistant",
                "content": error_message,
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })

if not st.session_state.messages:
    st.info("👋 Welcome! Ask me to perform calculations, search the web, execute code, or summarize PDFs.")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🎯 Quick Start")
        st.markdown("""
        - **Math**: "What is 25% of 840?"
        - **Code**: "Generate fibonacci numbers up to 100"
        - **Search**: "Find information about quantum computing"
        - **PDF**: "Summarize the document at pdfs/sample.pdf"
        """)
    
    
