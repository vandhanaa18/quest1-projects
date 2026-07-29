from google.adk.tools import FunctionTool
from ddgs import DDGS


def ddg_search(query: str) -> str:
    """
    Search the web using DuckDuckGo for information relevant to the
    user's research task.

    Args:
        query: The search query.

    Returns:
        Relevant web search results including titles, URLs, and summaries.
    """

    try:
        results = DDGS().text(
            query,
            max_results=2,
        )

        if not results:
            return f"No search results found for '{query}'."

        output = ["Search Results"]

        for index, result in enumerate(results, start=1):
            title = result.get("title", "No title")
            url = result.get("href", "No URL")
            summary = result.get("body", "No summary available")

            output.append(
                f"""
{index}. {title}
URL: {url}
Summary: {summary}
"""
            )

        return "\n".join(output)

    except Exception as error:
        return f"Search failed: {error}"


ddg_search_tool = FunctionTool(func=ddg_search)