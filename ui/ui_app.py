import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from agent import agent

st.set_page_config(page_title="LLM Agent Demo", layout="wide")
st.title("🤖 LLM Agent")

# Session state for managing input and response
if "query" not in st.session_state:
    st.session_state.query = ""
if "response" not in st.session_state:
    st.session_state.response = ""

# Input box bound to session_state
st.session_state.query = st.text_input("Enter your task:", value=st.session_state.query)

if st.button("Run Agent"):
    if st.session_state.query:
        with st.spinner("Thinking..."):
            try:
                st.session_state.response = agent.run(st.session_state.query)
                st.session_state.query = ""  # Clear input after processing
            except Exception as e:
                st.session_state.response = f"❌ Error: {e}"

# Show response if available
if st.session_state.response:
    st.success("Response:")
    st.write(st.session_state.response)
