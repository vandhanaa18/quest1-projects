from google.adk.tools import FunctionTool


def review_code(code: str) -> str:
    """
    Perform a basic static review of Python code and provide feedback.

    Args:
        code: Python source code to review.

    Returns:
        A formatted review report.
    """

    comments = []

    # Exception handling
    if "try:" not in code:
        comments.append("- Consider adding exception handling using try/except blocks.")

    # Functions
    if "def " not in code:
        comments.append("- Organize the code into reusable functions.")

    # Documentation
    if '"""' not in code and "'''" not in code:
        comments.append("- Add docstrings to improve code readability.")

    # Comments
    if "#" not in code:
        comments.append("- Include comments for complex logic.")

    # Main guard
    if "__name__" not in code:
        comments.append("- Consider using 'if __name__ == \"__main__\":' as the program entry point.")

    # Empty code
    if not code.strip():
        return "Review Report\n\nThe submitted code is empty."

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