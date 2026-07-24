from google.adk.tools import FunctionTool
import io
import contextlib


def execute_code(code: str) -> str:
    """
    Execute Python code and return its output or any errors.

    Args:
        code: Python source code to execute.

    Returns:
        The execution output or an error message.
    """

    output = io.StringIO()

    try:
        with contextlib.redirect_stdout(output):
            exec(code, {})

        result = output.getvalue().strip()

        if result:
            return f"Execution Output:\n{result}"

        return "Code executed successfully with no output."

    except Exception as e:
        return f"Execution Failed:\n{type(e).__name__}: {e}"


execution_tool = FunctionTool(func=execute_code)