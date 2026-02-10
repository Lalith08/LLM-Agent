# LLM-Agent
A conversational AI agent powered by LangChain and OpenAI that can perform various tasks including calculations, code execution, web searches, and PDF summarization.

<img width="2232" height="1163" alt="image" src="https://github.com/user-attachments/assets/ccb44678-bd84-412d-99b7-149efb8dfb0e" />


## Setup Instructions

### Step 1: Create & Activate Virtual Environment
In your command prompt or terminal, run the following commands:

```bash
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Mac/Linux
```

### Step 2: Install Dependencies
Install the required dependencies by running:

```bash
pip install -r requirements.txt
```

**Note**: If you encounter errors with specific packages, manually install them:

```bash
pip install langchain langchain-community langchain-openai streamlit gradio duckduckgo-search PyPDF2 openai
```

### Step 3: Environment Variables
Create a `.env` file in the root directory and add your OpenAI API key:

```
OPENAI_API_KEY=your_openai_api_key_here
```

## Project File Structure
```
llm-agent-assignment/
├── agent.py
├── ui/
│   └── ui_app.py
├── tools/
│   ├── calculator.py
│   ├── code_executor.py
│   ├── summarizer.py
│   └── web_search.py
├── memory/
│   └── chat_memory.db
├── pdfs/
│   └── sample.pdf
├── .env
└── requirements.txt
```

## Running the Agent

### Run CLI Agent
To run the command-line interface agent:

```bash
python agent.py
```

### Run UI Agent
To run the user interface agent (Streamlit):

```bash
streamlit run ui/ui_app.py
```

## Agent Features

- **Calculator Tool**: Safe mathematical expression evaluation with support for basic operations and functions
- **Code Executor**: Sandboxed Python code execution environment
- **Web Search**: DuckDuckGo-powered web search capability
- **PDF Summarizer**: Extract and summarize content from PDF documents
- **Conversational Memory**: Maintains conversation history using SQLite
- **Web UI**: Streamlit-based user interface

### Memory
- **Short-term Memory**: In-session context using `ConversationBufferMemory`.
- **Long-term Memory**: Persistent chat history stored in `SQLChatMessageHistory` (SQLite-based).


 ## Notes

- Conversation history is stored in `chat_memory.db`
- The agent maintains context across multiple interactions
- All tools include error handling and validation


## 🤝 Contributing

Feel free to submit issues or pull requests for improvements.
