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

Review the implementation created by the Code Generator.

PLANNER HANDOFF:
{planner_output}

CODE GENERATOR HANDOFF:
{code_output}

Review the actual implementation/files.

Return exactly:

REVIEW_STATUS:
<PASS or FAIL>

ISSUES:
<issues or None>

REQUIRED_FIXES:
<fixes or None>

HANDOFF_TO_TEST:
<information required by Test Agent>
After completing your work, call transfer_to_agent to return
control to software_development_coordinator. Do not end your
turn without performing this transfer.
""",

    output_key="reviewer_output",

    before_agent_callback=before_agent,
    after_agent_callback=after_agent,

    tools=[
        review_tool,
    ],
)