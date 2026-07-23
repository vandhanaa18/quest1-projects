from google.adk.tools import FunctionTool


def get_documentation(topic: str):
    """
    Retrieve technical documentation.
    """
    return f"Documentation for: {topic}"


documentation_tool = FunctionTool(func=get_documentation)