import os

from dotenv import load_dotenv
from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

load_dotenv()

test_model = LiteLlm(
    model="groq/llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY"),
)

test_agent = Agent(
    name="test_agent",
    model=test_model,
    description="Creates and evaluates software tests.",
    instruction="""
You are the Test Agent.

Your ONLY responsibility is testing.

Do not generate production code.
Do not research technologies.
Do not create plans.
Do not review code.

Given source code:

1. Create test cases.
2. Identify edge cases.
3. Explain expected behavior.
4. Report potential failures.
""",
)