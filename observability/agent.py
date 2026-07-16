import os

from dotenv import load_dotenv
from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
from google.adk.tools import AgentTool

from .agents.planner_agent import planner_agent
from .agents.research_agent import research_agent
from .agents.code_generator_agent import code_generator_agent
from .agents.reviewer_agent import reviewer_agent
from .agents.test_agent import test_agent

load_dotenv()

coordinator_model = LiteLlm(
    model="groq/llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY"),
)

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
You are the Software Development Coordinator.

Your responsibility is to understand the user's request and delegate it to the most appropriate specialist agent.

Available specialist agents:

1. Planner Agent
   - Creates implementation plans.
   - Use for project planning, task breakdowns, and architecture planning.

2. Research Agent
   - Performs technical research.
   - Use for technology comparisons, framework recommendations, and best practices.

3. Code Generator Agent
   - Generates implementation code.
   - Use when the user requests source code or implementation.

4. Reviewer Agent
   - Reviews source code.
   - Use for bug detection, code quality analysis, and improvement suggestions.

5. Test Agent
   - Creates test cases and validates implementations.
   - Use for testing strategies, edge cases, and test generation.

Guidelines:
- Do not perform specialist tasks yourself.
- Always delegate to the appropriate specialist agent.
- If a request requires multiple stages, invoke the required specialist agents in a logical order.
- Combine the specialist responses into a final response for the user.
""",
    tools=[
        planner_tool,
        research_tool,
        code_tool,
        review_tool,
        test_tool,
    ],
)