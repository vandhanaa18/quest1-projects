from google.adk.agents import Agent

from ..providers.llm_provider import ModelProvider
from ..telemetry.callbacks import (
    before_agent,
    after_agent,
)

from ..tools.google_search_tool import google_search_tool
from ..tools.documentation_tool import documentation_tool
from ..tools.api_search_tool import api_search_tool

research_agent = Agent(
    name="research_agent",
    model=ModelProvider.get_model(),
    description="Researches technologies and provides technical recommendations.",
    instruction="""
You are the Research Agent.

Your responsibilities are:

1. Research relevant technologies.
2. Compare suitable options.
3. Recommend the best approach.
4. Use the Google Search Tool when web information is required.
5. Use the Documentation Tool to retrieve official documentation.
6. Use the API Search Tool to find suitable APIs.

Do not generate code.
Do not create implementation plans.
Do not review code.
Do not test code.
""",
    before_agent_callback=before_agent,
    after_agent_callback=after_agent,
    tools=[
        google_search_tool,
        documentation_tool,
        api_search_tool,
    ],
)