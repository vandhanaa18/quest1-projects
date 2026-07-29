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

Create a concise implementation plan for the user's software development task.

Rules:
- Identify the required deliverables.
- Create clear, actionable implementation steps.
- Include only the agents required to execute the plan.
- For continuation tasks, load previous workflow information when needed.
- Save the workflow after creating the plan.
- Update the workflow status after planning.
- Do not generate code, research, review, or test.
- Do not explain reasoning or workflow decisions.
- Keep the plan concise and preserve the user's requirements.

Return only:

Task Summary:
<concise summary>

Implementation Plan:
1. ...
2. ...
3. ...

Execution Plan:
<required agents in execution order>
""",
    before_agent_callback=before_agent,
    after_agent_callback=after_agent,
    tools=[
        save_workflow_tool,
        load_workflow_tool,
        update_workflow_status_tool,
    ],
)