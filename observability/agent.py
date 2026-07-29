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
You coordinate the software development workflow.

Delegate the user's request only to the agents required to complete it.

Rules:
- Do not perform specialist work yourself.
- Do not explain reasoning or delegation.
- Do not call unnecessary agents.
- Preserve the user's requirements.
- Continue until the requested task is complete.
- Return the actual result, not workflow details.
""",
    sub_agents=[
        planner_agent,
        research_agent,
        code_generator_agent,
        reviewer_agent,
        test_agent,
    ],
)