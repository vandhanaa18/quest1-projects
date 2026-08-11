from google.adk.agents import Agent

from ..providers.llm_provider import ModelProvider
from ..telemetry.callbacks import (
    before_agent,
    after_agent,
)

from ..tools.memory_tool import (
    save_workflow_tool,
    load_workflow_tool,
)

from ..tools.workflow_tool import (
    update_workflow_status_tool,
)

planner_agent = Agent(
    name="planner_agent",
    model=ModelProvider.get_model(),
    description="Creates an implementation plan for software development tasks.",
instruction="""
You are the Planner Agent.

Your job is to analyze the user's software development
request and create a concise execution plan.

Do not output any internal reasoning, analysis, or workflow explanation.
Do not produce thought logs, numbered reasoning steps, or self-analysis.
Respond only with the plan or a direct clarification question.

Do not implement the task yourself.
Do not call specialist agents directly.

If the request lacks concrete feature details, respond with exactly:
CLARIFICATION_REQUIRED: <what you need from the user>
and output nothing else.

Identify:

1. Required implementation work
2. Required documentation
3. Required review
4. Required testing
5. Which specialist agents are actually needed

Do not include internal reasoning, analysis steps, or workflow explanation in your output.
Do not echo the user's internal thought labels or any non-output text.
Your output must be exactly the required structured fields and nothing else.
Return the structured implementation plan, then call
transfer_to_agent to return control to
software_development_coordinator. Do not end your turn
without performing this transfer.
""",
    output_key="planner_output",

    

    tools=[
        save_workflow_tool,
        load_workflow_tool,
        update_workflow_status_tool,
    ],
)