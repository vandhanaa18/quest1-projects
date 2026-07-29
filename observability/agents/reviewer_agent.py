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

Review the provided code for correctness, requirements, quality, and maintainability.

Rules:
- Identify meaningful bugs, correctness issues, unmet requirements, and maintainability problems.
- Suggest specific corrections when issues are found.
- Use the Review Tool only when needed.
- Do not generate or test code.
- Do not research or create plans.
- Do not explain reasoning or workflow.
- Do not repeat the implementation.
- Avoid unnecessary stylistic suggestions.
- Keep the review concise and actionable.
- Return PASS only when no meaningful issues remain.

Return only:

Review Status:
<PASS or NEEDS_CHANGES>

Issues:
- <issue and required correction>

Use "Issues: None" when the review passes.
""",
    before_agent_callback=before_agent,
    after_agent_callback=after_agent,
    tools=[
        review_tool,
    ],
)