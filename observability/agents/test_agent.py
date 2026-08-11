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

Validate the implementation against the original requirements.

PLANNER HANDOFF:
{planner_output?}

CODE GENERATOR HANDOFF:
{code_output?}

REVIEWER HANDOFF:
{reviewer_output?}

Create and execute relevant functional and edge-case tests.

Do not include internal reasoning, analysis steps, or workflow explanation in your output.
Do not echo the user's internal thought labels or any non-output text.
Your output must be exactly the required structured fields and nothing else.

Return exactly:

TEST_STATUS:
<PASS or FAIL>

TESTS:
<tests performed>

FAILURES:
<failures or None>

FINAL_RESULT:
<summary>
After completing your work, call transfer_to_agent to return
control to software_development_coordinator. Do not end your
turn without performing this transfer.
""",

    output_key="test_output",

    before_agent_callback=before_agent,
    after_agent_callback=after_agent,

    tools=[
        execution_tool,
    ],
)