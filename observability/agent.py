from google.adk.agents import Agent
from google.adk.tools import AgentTool

from .providers.llm_provider import ModelProvider

from .agents.planner_agent import planner_agent
from .agents.research_agent import research_agent
from .agents.code_generator_agent import code_generator_agent
from .agents.reviewer_agent import reviewer_agent
from .agents.test_agent import test_agent

# Use the shared model from ModelProvider
coordinator_model = ModelProvider.get_model()

# Wrap specialist agents as tools
planner_tool = AgentTool(planner_agent)
research_tool = AgentTool(research_agent)
code_tool = AgentTool(code_generator_agent)
review_tool = AgentTool(reviewer_agent)
test_tool = AgentTool(test_agent)

root_agent = Agent(
    name="software_development_coordinator",
    model=coordinator_model,
    description="Coordinates the software development workflow.",
    instruction="""
You are the Root Agent responsible for coordinating the software development workflow.

Your responsibilities are:

1. Understand the user's request.
2. Determine whether the request is:
   - A new task
   - A continuation of an existing task
3. Always consult the Planner Agent first.
4. Based on the Planner Agent's execution plan, invoke the required specialist agents in the correct order.
5. Combine the outputs from all invoked agents into a final response.

Available specialist agents:

- Planner Agent
- Research Agent
- Code Generator Agent
- Reviewer Agent
- Test Agent

Rules:
- Never perform specialist tasks yourself.
- The Planner Agent decides the workflow.
- Invoke only the agents required for the current request.
- Preserve workflow context across multi-turn conversations whenever possible.
""",
    tools=[
        planner_tool,
        research_tool,
        code_tool,
        review_tool,
        test_tool,
    ],
)