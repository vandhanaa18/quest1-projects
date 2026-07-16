import os

from dotenv import load_dotenv
from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

load_dotenv()

code_generator_model = LiteLlm(
    model="groq/llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY"),
)

code_generator_agent = Agent(
    name="code_generator_agent",
    model=code_generator_model,
    description="Generates code from implementation requirements.",
    instruction="""
You are the Code Generator Agent.

Your ONLY responsibility is generating code.

Do not create plans.
Do not research technologies.
Do not review code.
Do not test code.

Given a software requirement:

1. Generate clean code.
2. Use best practices.
3. Add comments where useful.
4. Return only the implementation.
""",
)