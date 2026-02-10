from langchain.tools import tool
import io
import contextlib
import math

@tool
def code_executor_tool(code: str) -> str:
    """Executes Python code in a sandboxed environment. Only allows safe operations like math, string manipulation, and basic data structures. No file I/O, network access, or system calls."""
    
    safe_builtins = {
        'abs': abs,
        'all': all,
        'any': any,
        'bool': bool,
        'dict': dict,
        'enumerate': enumerate,
        'filter': filter,
        'float': float,
        'int': int,
        'len': len,
        'list': list,
        'map': map,
        'max': max,
        'min': min,
        'pow': pow,
        'range': range,
        'reversed': reversed,
        'round': round,
        'set': set,
        'sorted': sorted,
        'str': str,
        'sum': sum,
        'tuple': tuple,
        'zip': zip,
        'print': print,
        'True': True,
        'False': False,
        'None': None,
    }
    
    safe_modules = {
        'math': math,
    }
    
    restricted_keywords = ['import', 'open', 'exec', 'eval', 'compile', '__import__', 'globals', 'locals', 'vars', 'dir', 'getattr', 'setattr', 'delattr', 'hasattr']
    
    for keyword in restricted_keywords:
        if keyword in code:
            return f"Security Error: Use of '{keyword}' is not allowed in sandboxed execution."
    
    output_buffer = io.StringIO()
    try:
        safe_globals = {'__builtins__': safe_builtins}
        safe_globals.update(safe_modules)
        
        with contextlib.redirect_stdout(output_buffer):
            exec(code, safe_globals, {})
        
        result = output_buffer.getvalue()
        return f"Output:\n{result}" if result else "Code executed with no output."
    except NameError as e:
        return f"Execution Error: {str(e)}. Note: Only safe built-in functions and the 'math' module are available."
    except Exception as e:
        return f"Execution Error: {str(e)}"
