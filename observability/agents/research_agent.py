from google.adk.agents import Agent

from ..providers.llm_provider import ModelProvider

research_agent = Agent(
    name="research_agent",
    model=ModelProvider.get_model(),
    description="Researches technologies and provides technical recommendations.",
    instruction="""
You are the Research Agent.

Your ONLY responsibility is to perform technical research.

Do not create implementation plans.
Do not generate code.
Do not review code.
Do not test code.

Given the user's request:

1. Research relevant technologies.
2. Compare suitable options.
3. Recommend the best approach.
4. Explain your reasoning clearly.
""",
)