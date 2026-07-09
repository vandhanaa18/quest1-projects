from pydantic import BaseModel


class OrderSchema(BaseModel):
    order_id: str
    item: str
    quantity: int
    amount: int