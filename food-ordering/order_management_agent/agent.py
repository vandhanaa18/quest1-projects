from .tools.order_tool import (
    create_order,
    show_order_history,
    update_order,
    cancel_order,
    get_food_variants
)

from google.adk.agents import Agent
from .prompt import ORDER_PROMPT


order_agent = Agent(
    name="order_management_agent",
    model="gemini-2.5-flash",
    description="Handles ordering operations",

    instruction=ORDER_PROMPT,

    tools=[
        get_food_variants,
        create_order,
        show_order_history,
        update_order,
        cancel_order
    ]
)