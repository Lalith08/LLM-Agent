from langchain.tools import tool

@tool
def calculator_tool(expression: str) -> str:
    """Evaluate a basic math expression passed as a string."""
    try:
        result = eval(expression)
        return f"Result: {result}"
    except Exception as e:
        return f"Error: {str(e)}"
