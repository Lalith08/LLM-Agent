# LLM-Agent
An LLM-based agent

![image](https://github.com/user-attachments/assets/aba1ea9e-8d45-4221-b968-b963e120cc46)


Setup Instructions:

Step 1: Create & Activate Virtual Environment in CMD Prompt


python -m venv venv


venv\Scripts\activate   # Windows


# source venv/bin/activate   # Mac/Linux

Step 2 : Install Dependencies

pip install -r requirements.txt

Note
if you see errors with specific packages, manually install them:

pip install langchain langchain-community langchain-openai streamlit gradio duckduckgo-search PyPDF2 openai


Step 3: Environment Variables
Create a .env file in the root directory and add the below line
OPENAI_API_KEY=your_openai_api_key_here


Project File Structure

llm-agent-assignment/
 agent.py                  
 ui/ ui_app.py             
 tools/
      calculator.py
      code_executor.py
      summarizer.py
      web_search.py
 memory                  
     chat_memory.db
 pdfs/sample.pdf

                         
 .env                    
  requirements.txt

Run CLI Agent 
python agent.py

Run UI Agent
Streamlit run ui\ui_app.py

Agent Features
Tools Integrated:
calculator_tool – Evaluates math expressions


code_executor_tool – Runs basic Python code snippets


web_search_tool – Uses DuckDuckGo to find web info


summarizer_tool – Summarizes contents of PDF files


Memory:
Short-term memory: In-session context using ConversationBufferMemory


Long-term memory: Persistent chat history via SQLChatMessageHistory (SQLite-based)
