from google.adk.tools import FunctionTool


def review_code(code: str):
    comments = []

    if "try:" not in code:
        comments.append("Add exception handling.")

    if "def " not in code:
        comments.append("Use functions.")

    return comments


review_tool = FunctionTool(func=review_code)