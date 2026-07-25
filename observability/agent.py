from google.adk.agents import Agent

from .providers.llm_provider import ModelProvider

from .agents.planner_agent import planner_agent
from .agents.research_agent import research_agent
from .agents.code_generator_agent import code_generator_agent
from .agents.reviewer_agent import reviewer_agent
from .agents.test_agent import test_agent

# Shared model
coordinator_model = ModelProvider.get_model()

root_agent = Agent(
    name="software_development_coordinator",
    model=coordinator_model,
    description="Coordinates the software development workflow.",
    instruction="""
You are the Root Agent responsible for coordinating the software development workflow.

Your responsibilities are:

1. Understand the user's request.
2. Determine whether it is a new task or a continuation.
3. Delegate work to the appropriate sub-agent.
4. Coordinate the overall workflow.
5. Combine the outputs from sub-agents into the final response.

Available sub-agents:
- Planner Agent
- Research Agent
- Code Generator Agent
- Reviewer Agent
- Test Agent

Rules:
- Never perform specialist tasks yourself.
- Delegate work to the appropriate sub-agent.
- Invoke only the required sub-agents.
- Preserve workflow context whenever possible.
""",
    sub_agents=[
        planner_agent,
        research_agent,
        code_generator_agent,
        reviewer_agent,
        test_agent,
    ],
)