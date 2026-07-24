from google.adk.tools import FunctionTool


def generate_code(requirement: str) -> str:
    """
    Provide code templates or starter snippets for common programming tasks.

    Args:
        requirement: Description of the programming task.

    Returns:
        A relevant code template or boilerplate.
    """

    requirement = requirement.lower()

    if "stack" in requirement and "python" in requirement:
        return """
Python Stack Template

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.items:
            return self.items.pop()
        return None

    def peek(self):
        return self.items[-1] if self.items else None

    def is_empty(self):
        return len(self.items) == 0
"""

    elif "queue" in requirement and "python" in requirement:
        return """
from collections import deque

queue = deque()

queue.append(10)
queue.append(20)

queue.popleft()
"""

    elif "flask" in requirement:
        return """
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World!"

if __name__ == "__main__":
    app.run(debug=True)
"""

    else:
        return "No template available for the requested requirement."


code_editor_tool = FunctionTool(func=generate_code)