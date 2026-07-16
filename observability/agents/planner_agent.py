import os

from dotenv import load_dotenv
from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

load_dotenv()

planner_model = LiteLlm(
    model="groq/llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY"),
)

planner_agent = Agent(
    name="planner_agent",
    model=planner_model,
    description="Creates an implementation plan for software development tasks.",
    instruction="""
You are the Planner Agent.

Your ONLY responsibility is to create a clear implementation plan.

Do not generate code.
Do not research technologies.
Do not review code.
Do not test code.

Given the user's request:

1. Understand the task.
2. Break it into logical implementation steps.
3. Return a concise numbered plan.
""",
)