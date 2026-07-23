from google.adk.agents import Agent

from ..providers.llm_provider import ModelProvider
from ..telemetry.callbacks import (
    before_agent,
    after_agent,
)

from ..tools.review_tool import (
    review_tool,
)

reviewer_agent = Agent(
    name="reviewer_agent",
    model=ModelProvider.get_model(),
    description="Reviews code quality and identifies issues.",
    instruction="""
You are the Reviewer Agent.

Your responsibilities are:

1. Review source code.
2. Identify bugs.
3. Detect code smells.
4. Suggest improvements.
5. Use the Review Tool to analyze code quality.

Do not generate code.
Do not research technologies.
Do not create implementation plans.
Do not test code.

Return a clear review report with recommendations.
""",
    before_agent_callback=before_agent,
    after_agent_callback=after_agent,
    tools=[
        review_tool,
    ],
)