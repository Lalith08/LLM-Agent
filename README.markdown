# LLM-Agent
An LLM-based agent for performing various tasks using integrated tools and memory management.

![LLM Agent](https://github.com/user-attachments/assets/aba1ea9e-8d45-4221-b968-b963e120cc46)

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

### Tools Integrated
- **Calculator Tool**: Evaluates mathematical expressions.
- **Code Executor Tool**: Executes basic Python code snippets.
- **Web Search Tool**: Performs web searches using DuckDuckGo.
- **Summarizer Tool**: Summarizes the contents of PDF files.

### Memory
- **Short-term Memory**: In-session context using `ConversationBufferMemory`.
- **Long-term Memory**: Persistent chat history stored in `SQLChatMessageHistory` (SQLite-based).