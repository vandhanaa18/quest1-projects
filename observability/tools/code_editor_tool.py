from google.adk.tools import FunctionTool


def generate_code(requirement: str):
    """
    Generate source code.
    """
    return f"Generated code for: {requirement}"


code_editor_tool = FunctionTool(func=generate_code)