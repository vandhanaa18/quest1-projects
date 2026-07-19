from google.adk.agents import Agent

from ..providers.llm_provider import ModelProvider
from ..telemetry.callbacks import (
    before_agent,
    after_agent,
)

planner_agent = Agent(
    name="planner_agent",
    model=ModelProvider.get_model(),
    description="Creates an implementation plan for software development tasks.",
    instruction="""
You are the Planner Agent.

Your ONLY responsibility is to create a clear implementation plan.

Do not generate code.
Do not research technologies.
Do not review code.
Do not test code.

Given the user's request:

1. Understand the task.
2. Break it into logical implementation steps.
3. Return a concise numbered plan.
""",
    before_agent_callback=before_agent,
    after_agent_callback=after_agent,
)