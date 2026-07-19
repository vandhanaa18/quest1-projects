from google.adk.agents import Agent

from ..providers.llm_provider import ModelProvider

reviewer_agent = Agent(
    name="reviewer_agent",
    model=ModelProvider.get_model(),
    description="Reviews code quality and identifies issues.",
    instruction="""
You are the Reviewer Agent.

Your ONLY responsibility is reviewing code.

Do not generate code.
Do not research technologies.
Do not create plans.
Do not test code.

Given source code:

1. Identify bugs.
2. Identify code smells.
3. Suggest improvements.
4. Explain issues clearly.
""",
)