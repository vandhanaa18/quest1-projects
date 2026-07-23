from google.adk.tools import FunctionTool


def execute_code(code: str):
    """
    Execute generated code.
    """
    return "Execution successful"


execution_tool = FunctionTool(func=execute_code)