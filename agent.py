import os
from dotenv import load_dotenv
from langchain.agents import initialize_agent, AgentType
from langchain_community.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.memory.chat_message_histories import SQLChatMessageHistory
from tools.calculator import calculator_tool
from tools.code_executor import code_executor_tool
from tools.web_search import web_search_tool
from tools.summarizer import summarize_pdf



# Loading API Key
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

# Initialize the LLM
llm = ChatOpenAI(
    temperature=0,
    model="gpt-4o-mini",
    openai_api_key=openai_api_key
)

tools = [
    calculator_tool,
    code_executor_tool,
    web_search_tool,
    summarize_pdf,
]


# persistent memory store using SQLite
message_history = SQLChatMessageHistory(connection_string="sqlite:///chat_memory.db", session_id="user_1")

# Conversation memory that persists from all the sessions
memory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True,
    chat_memory=message_history
)



# Initialize agent
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION,
    memory=memory,
    verbose=True
)

# CLI to run agent
if __name__ == "__main__":
    print("🤖 LLM Agent is ready! Type your task or 'exit' to quit.\n")
    while True:
        query = input("🧠 Ask > ")
        if query.lower() in ["exit", "quit"]:
            break
        try:
            response = agent.run(query)
            print("\n🗣️ Response:\n", response)
        except Exception as e:
            print(f"\n❌ Error: {e}")






