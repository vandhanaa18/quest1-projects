from google.adk.tools import FunctionTool


def google_search(query: str) -> str:
    """
    Search the web for technical information related to a software development task.

    Args:
        query: The search query.

    Returns:
        A structured summary of relevant search results.
    """

    query = query.lower()

    if "stack" in query and "python" in query:
        return """
Search Results

1. Real Python - Using Stacks and Queues in Python
Summary:
Python lists provide an easy way to implement a stack using append() and pop().
For larger applications, collections.deque is recommended because of its efficient O(1) operations.

2. Python Official Documentation - collections.deque
Summary:
deque supports fast append() and pop() operations from either end and is suitable for implementing stacks and queues.

3. GeeksforGeeks - Stack in Python
Summary:
Demonstrates stack implementation using lists, deque, and queue.LifoQueue with examples and time complexity.
"""

    elif "binary search" in query:
        return """
Search Results

1. Python Binary Search Tutorial
Summary:
Binary search efficiently finds an element in a sorted list with O(log n) time complexity.

2. GeeksforGeeks
Summary:
Provides iterative and recursive implementations of binary search.
"""

    elif "fastapi" in query:
        return """
Search Results

1. FastAPI Official Documentation
Summary:
Modern Python framework for building high-performance REST APIs with automatic OpenAPI documentation.

2. FastAPI Tutorial
Summary:
Explains routing, dependency injection, request validation, and asynchronous programming.
"""

    else:
        return f"No relevant search results found for '{query}'."


google_search_tool = FunctionTool(func=google_search)