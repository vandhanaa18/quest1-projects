from google.adk.tools import FunctionTool


def get_documentation(topic: str) -> str:
    """
    Retrieve concise technical documentation for a programming topic,
    library, framework, or concept.

    Args:
        topic: The topic for which documentation is requested.

    Returns:
        A concise documentation summary with key features and usage.
    """

    topic = topic.lower()

    if "stack" in topic and "python" in topic:
        return """
Python Stack Documentation

Definition:
A stack is a Last-In, First-Out (LIFO) data structure.

Recommended Implementations:
1. list
   - push: append()
   - pop: pop()
   - Suitable for most applications.

2. collections.deque
   - append()
   - pop()
   - Faster and more memory efficient for large-scale applications.

Common Operations:
- Push
- Pop
- Peek
- is_empty

Time Complexity:
Push : O(1)
Pop  : O(1)
Peek : O(1)
"""

    elif "deque" in topic:
        return """
collections.deque

Module:
collections

Purpose:
Provides a double-ended queue with efficient insertion and removal from both ends.

Important Methods:
- append()
- appendleft()
- pop()
- popleft()

Complexity:
All above operations execute in O(1) time.
"""

    elif "fastapi" in topic:
        return """
FastAPI

Purpose:
A modern Python web framework for building REST APIs.

Key Features:
- High performance
- Automatic OpenAPI documentation
- Type hints
- Async support
"""

    else:
        return f"""
Documentation for: {topic}

No specific documentation is available.

Suggestions:
- Refer to the official documentation.
- Search for practical examples.
- Review best practices before implementation.
"""


documentation_tool = FunctionTool(func=get_documentation)