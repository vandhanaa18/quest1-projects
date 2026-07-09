from .tools.payment_tool import verify_payment
from google.adk.agents import Agent
from payment_verification_agent.prompt import PAYMENT_PROMPT
from payment_verification_agent.tools.payment_tool import verify_payment

payment_agent = Agent(
    name="payment_verification_agent",
    model="gemini-2.5-flash",
    description="Verifies payment status for food orders.",
    instruction=PAYMENT_PROMPT,
    tools=[verify_payment]
)