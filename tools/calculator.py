from langchain.tools import tool
import ast
import operator
import math

@tool
def calculator_tool(expression: str) -> str:
    """Evaluate a basic math expression passed as a string. Supports +, -, *, /, **, %, sqrt, sin, cos, tan, log, and parentheses."""
    
    allowed_operators = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv,
        ast.Pow: operator.pow,
        ast.Mod: operator.mod,
        ast.USub: operator.neg,
        ast.UAdd: operator.pos,
    }
    
    allowed_functions = {
        'sqrt': math.sqrt,
        'sin': math.sin,
        'cos': math.cos,
        'tan': math.tan,
        'log': math.log,
        'log10': math.log10,
        'exp': math.exp,
        'abs': abs,
        'round': round,
    }
    
    def safe_eval(node):
        if isinstance(node, ast.Num):
            return node.n
        elif isinstance(node, ast.Constant):
            return node.value
        elif isinstance(node, ast.BinOp):
            left = safe_eval(node.left)
            right = safe_eval(node.right)
            op = allowed_operators.get(type(node.op))
            if op is None:
                raise ValueError(f"Operator {type(node.op).__name__} not allowed")
            return op(left, right)
        elif isinstance(node, ast.UnaryOp):
            operand = safe_eval(node.operand)
            op = allowed_operators.get(type(node.op))
            if op is None:
                raise ValueError(f"Unary operator {type(node.op).__name__} not allowed")
            return op(operand)
        elif isinstance(node, ast.Call):
            func_name = node.func.id if isinstance(node.func, ast.Name) else None
            if func_name not in allowed_functions:
                raise ValueError(f"Function '{func_name}' not allowed")
            args = [safe_eval(arg) for arg in node.args]
            return allowed_functions[func_name](*args)
        else:
            raise ValueError(f"Expression type {type(node).__name__} not allowed")
    
    try:
        expression = expression.strip()
        tree = ast.parse(expression, mode='eval')
        result = safe_eval(tree.body)
        return f"Result: {result}"
    except SyntaxError as e:
        return f"Syntax Error: Invalid mathematical expression - {str(e)}"
    except ValueError as e:
        return f"Error: {str(e)}"
    except ZeroDivisionError:
        return "Error: Division by zero"
    except Exception as e:
        return f"Error: {str(e)}"
