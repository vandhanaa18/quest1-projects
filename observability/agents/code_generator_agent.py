from google.adk.agents import Agent

from ..providers.llm_provider import ModelProvider
from ..telemetry.callbacks import (
    before_agent,
    after_agent,
)

code_generator_agent = Agent(
    name="code_generator_agent",
    model=ModelProvider.get_model(),
    description="Generates code from implementation requirements.",
    instruction="""
You are the Code Generator Agent.

Your ONLY responsibility is generating code.

Do not create plans.
Do not research technologies.
Do not review code.
Do not test code.

Given a software requirement:

1. Generate clean code.
2. Use best practices.
3. Add comments where useful.
4. Return only the implementation.
""",
    before_agent_callback=before_agent,
    after_agent_callback=after_agent,
)