from langchain.tools import tool
from duckduckgo_search import DDGS

@tool
def web_search_tool(query: str) -> str:
    """Performs a web search using DuckDuckGo and returns the top result snippet."""
    try:
        with DDGS() as ddgs:
            results = ddgs.text(query, max_results=1)
            for result in results:
                return f"Title: {result['title']}\nSnippet: {result['body']}\nLink: {result['href']}"
        return "No results found."
    except Exception as e:
        return f"Search Error: {str(e)}"
