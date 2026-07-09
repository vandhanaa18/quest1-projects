from google.adk.agents import Agent
from .prompt import RESTAURANT_PROMPT
from .tools.restaurant_tool import get_nearby_restaurants


restaurant_agent = Agent(
    name="restaurant_agent",
    model="gemini-2.5-flash",
    instruction=RESTAURANT_PROMPT,
    tools=[get_nearby_restaurants]
)