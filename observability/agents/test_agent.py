from google.adk.agents import Agent

from ..providers.llm_provider import ModelProvider
from ..telemetry.callbacks import (
    before_agent,
    after_agent,
)

from ..tools.execution_tool import (
    execution_tool,
)

test_agent = Agent(
    name="test_agent",
    model=ModelProvider.get_model(),
    description="Creates and evaluates software tests.",
    instruction="""
You are the Test Agent.

Your responsibilities are:

1. Create test cases.
2. Identify edge cases.
3. Explain expected behavior.
4. Report potential failures.
5. Use the Execution Tool to execute and validate code when required.

Do not generate production code.
Do not research technologies.
Do not create implementation plans.
Do not review code.

Return a structured testing report.
""",
    before_agent_callback=before_agent,
    after_agent_callback=after_agent,
    tools=[
        execution_tool,
    ],
)