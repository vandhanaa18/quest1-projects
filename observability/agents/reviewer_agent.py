import os

from dotenv import load_dotenv
from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

load_dotenv()

reviewer_model = LiteLlm(
    model="groq/llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY"),
)

reviewer_agent = Agent(
    name="reviewer_agent",
    model=reviewer_model,
    description="Reviews code quality and identifies issues.",
    instruction="""
You are the Reviewer Agent.

Your ONLY responsibility is reviewing code.

Do not generate code.
Do not research technologies.
Do not create plans.
Do not test code.

Given source code:

1. Identify bugs.
2. Identify code smells.
3. Suggest improvements.
4. Explain issues clearly.
""",
)