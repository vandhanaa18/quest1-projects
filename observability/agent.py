import os

from dotenv import load_dotenv
from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
from google.adk.tools import AgentTool

from .agents.planner_agent import planner_agent
from .agents.research_agent import research_agent

load_dotenv()

coordinator_model = LiteLlm(
    model="groq/llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY"),
)

planner_tool = AgentTool(planner_agent)
research_tool = AgentTool(research_agent)

root_agent = Agent(
    name="software_development_coordinator",
    model=coordinator_model,
    description="Coordinates the software development workflow.",
    instruction="""
You are the Coordinator Agent.

Your responsibility is to understand the user's request and decide which specialist
agent should handle it.

Available specialists:

- Planner Agent
    Use for implementation plans.

- Research Agent
    Use for technology research, comparisons and recommendations.

Always use the appropriate specialist agent instead of answering yourself whenever possible.
""",
    tools=[
        planner_tool,
        research_tool,
    ],
)