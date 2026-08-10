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

Do not implement the task yourself.
Do not call specialist agents directly.

Identify:

1. Required implementation work
2. Required documentation
3. Required review
4. Required testing
5. Which specialist agents are actually needed

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