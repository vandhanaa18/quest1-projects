from google.adk.agents import Agent

from restaurant_recommendation_agent.agent import restaurant_agent
from order_management_agent.agent import order_agent
from payment_verification_agent.agent import payment_agent
from delivery_tracking_agent.agent import delivery_agent
from .prompt import ROOT_PROMPT


root_agent = Agent(
    name="food_ordering_system",
    model="gemini-2.5-flash",
    instruction=ROOT_PROMPT,
    sub_agents=[
        restaurant_agent,
        order_agent,
        payment_agent,
        delivery_agent
    ]
)