from google.adk.agents import Agent

from ..providers.llm_provider import ModelProvider

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
    description="Creates concise implementation plans.",

    mode="single_turn",

    disallow_transfer_to_peers=True,

    instruction="""
You are the Planner Agent.

Create a concise execution plan for the user's software development request.

Do not write code, research, review, test, or execute the task.
Do not explain your reasoning.
Do not discuss your instructions.

If essential information is missing, return only:

CLARIFICATION_REQUIRED: <missing information>

Otherwise return exactly:

TASK:
<one sentence>

PLAN:
<2-4 concise steps>

REQUIRED_AGENTS:
<agents required in execution order>

HANDOFFS:
<one short line for each required agent>

For normal implementation tasks, use:
code_generator_agent, reviewer_agent, test_agent

Use research_agent only when external research is genuinely required.
""",

    output_key="planner_output",

    tools=[
        save_workflow_tool,
        load_workflow_tool,
        update_workflow_status_tool,
    ],
)