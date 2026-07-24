from google.adk.tools import FunctionTool


def api_search(task: str) -> str:
    """
    Recommend suitable APIs or libraries for a given software development task.

    Args:
        task: Description of the task or functionality.

    Returns:
        A list of relevant APIs/libraries with a brief explanation.
    """

    task = task.lower()

    if "stack" in task and "python" in task:
        return """
Recommended Library:
- collections.deque
  Purpose: Efficient stack and queue implementation.
  Advantages:
    - O(1) append()
    - O(1) pop()
    - Memory efficient

Alternative:
- Python list
  Purpose: Simple stack implementation.
  Advantages:
    - Easy to use
    - Built-in support for append() and pop()
  Best for:
    - Small to medium-sized applications.
"""

    elif "weather" in task:
        return """
Recommended APIs:
- OpenWeatherMap API
  Purpose: Current weather and forecasts.

- WeatherAPI
  Purpose: Weather, air quality, astronomy, and forecasts.
"""

    elif "movie" in task:
        return """
Recommended APIs:
- TMDB API
  Purpose: Movies, TV shows, actors, ratings, recommendations.

- OMDb API
  Purpose: Movie information by title or IMDb ID.
"""

    else:
        return """
No specific API recommendation found.

General-purpose APIs/Libraries:
- REST APIs using FastAPI
- Requests library
- JSONPlaceholder (for testing)
"""


api_search_tool = FunctionTool(func=api_search)