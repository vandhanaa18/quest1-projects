from google.adk.tools import FunctionTool


def review_code(code: str) -> str:
    """
    Perform a basic static review of Python code.
    """

    if not code or not code.strip():
        return "Review Report\n\nThe submitted code is empty."

    comments = []

    if "def " not in code and "class " not in code:
        comments.append("- Consider organizing the implementation into reusable functions or classes.")

    if '"""' not in code and "'''" not in code:
        comments.append("- Consider adding docstrings.")

    if "__name__" not in code:
        comments.append("- Consider adding an if __name__ == '__main__' entry point when appropriate.")

    if not comments:
        return (
            "Review Report\n\n"
            "No major issues detected.\n"
            "The code follows basic Python coding practices."
        )

    return (
        "Review Report\n\n"
        "Suggestions:\n"
        + "\n".join(comments)
    )


review_tool = FunctionTool(func=review_code)