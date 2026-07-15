import os

from dotenv import load_dotenv
from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm


load_dotenv()


groq_model = LiteLlm(
    model="groq/llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY"),
)


planner_agent = Agent(
    name="planner_agent",
    model=groq_model,
    description="Creates a clear step-by-step plan for the user's task.",
    instruction="""
You are the Planner Agent in a multi-agent software development workflow.

Your responsibility is to:

1. Understand the user's task.
2. Break the task into clear and logical implementation steps.
3. Identify what the Research Agent should investigate.
4. Identify what the Code Generator Agent should implement.
5. Identify what the Reviewer Agent should review.
6. Identify what the Test Agent should test.

Return a concise and structured plan that can be passed to the next agent in the workflow.
""",
)