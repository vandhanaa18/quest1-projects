from google.adk.tools import FunctionTool


def google_search(query: str):
    """
    Search the web for relevant information.
    """
    return f"Google Search Results for: {query}"


google_search_tool = FunctionTool(func=google_search)