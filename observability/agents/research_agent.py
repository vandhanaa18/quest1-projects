from google.adk.agents import Agent

from ..providers.llm_provider import ModelProvider
from ..telemetry.callbacks import (
    before_agent,
    after_agent,
)

from ..tools.ddg_search_tool import ddg_search_tool


research_agent = Agent(
    name="research_agent",
    model=ModelProvider.get_model(),
    description="Researches topics and external information and provides concise findings and recommendations.",
    instruction="""
You are the Research Agent.

Research information required by the user's request.

Rules:
- Use DDG only when external information is required.
- Use at most 3 searches.
- Each search must target different needed information.
- Do not repeat similar searches.
- Stop searching once enough information is available.
- Keep findings concise.
- Do not generate code, plan, review, or test.
- Do not explain reasoning or workflow.

Return:

Research Findings:
- ...

Recommendation:
...
""",
    before_agent_callback=before_agent,
    after_agent_callback=after_agent,
    tools=[
        ddg_search_tool,
    ],
)