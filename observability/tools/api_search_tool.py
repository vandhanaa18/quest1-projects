from google.adk.tools import FunctionTool


def api_search(task: str):
    """
    Find suitable APIs.
    """
    return f"Suggested APIs for: {task}"


api_search_tool = FunctionTool(func=api_search)