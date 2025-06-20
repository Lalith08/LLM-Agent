from langchain.tools import tool
import io
import contextlib

@tool
def code_executor_tool(code: str) -> str:
    """Executes Python code and returns the output."""
    output_buffer = io.StringIO()

    try:
        with contextlib.redirect_stdout(output_buffer):
            exec(code, {})
        result = output_buffer.getvalue()
        return f"Output:\n{result}" if result else "Code executed with no output."
    except Exception as e:
        return f"Execution Error: {str(e)}"
