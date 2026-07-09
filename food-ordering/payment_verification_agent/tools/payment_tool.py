import random
import time
from datetime import datetime

def verify_payment(order_id: str, amount: int):

    status = random.choice(["Success", "Pending", "Failed"])

    if status == "Pending":
        time.sleep(3)
        status = random.choice(["Success", "Failed"])

    payment = {
        "payment_id": f"PAY{random.randint(1000,9999)}",
        "order_id": order_id,
        "amount": amount,
        "status": status,
        "timestamp": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    }

    return payment