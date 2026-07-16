import os

from dotenv import load_dotenv
from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

load_dotenv()

research_model = LiteLlm(
    model="groq/llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY"),
)

research_agent = Agent(
    name="research_agent",
    model=research_model,
    description="Researches technologies and provides technical recommendations.",
    instruction="""
You are the Research Agent.

Your ONLY responsibility is to perform technical research.

Do not create implementation plans.
Do not generate code.
Do not review code.
Do not test code.

Given the user's request:

1. Research relevant technologies.
2. Compare suitable options.
3. Recommend the best approach.
4. Explain your reasoning clearly.
""",
)