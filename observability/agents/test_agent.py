from google.adk.agents import Agent

from ..providers.llm_provider import ModelProvider
from ..telemetry.callbacks import (
    before_agent,
    after_agent,
)

test_agent = Agent(
    name="test_agent",
    model=ModelProvider.get_model(),
    description="Creates and evaluates software tests.",
    instruction="""
You are the Test Agent.

Your ONLY responsibility is testing.

Do not generate production code.
Do not research technologies.
Do not create plans.
Do not review code.

Given source code:

1. Create test cases.
2. Identify edge cases.
3. Explain expected behavior.
4. Report potential failures.
""",
    before_agent_callback=before_agent,
    after_agent_callback=after_agent,
)