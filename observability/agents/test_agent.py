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

Validate whether the provided implementation satisfies the required behavior.

Rules:
- Create relevant functional and edge-case tests.
- Determine the expected result for each test.
- Use the Execution Tool when code execution is needed.
- Do not modify production code.
- Do not research, plan, or perform general code review.
- Do not explain reasoning or workflow.
- Do not repeat the implementation.
- Keep tests focused and concise.
- Return PASS only if all required tested behavior works.
- Clearly report any failing behavior or execution error.

Return only:

Test Status:
<PASS or FAIL>

Tests:
- <test>: <PASS or FAIL>

Failures:
- <failure details>

Use "Failures: None" when all tests pass.
""",
    before_agent_callback=before_agent,
    after_agent_callback=after_agent,
    tools=[
        execution_tool,
    ],
)