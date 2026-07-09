delivery_status = {}

def track_delivery(order_id: str):

    stages = [
        "Order Confirmed",
        "Preparing Food",
        "Out For Delivery",
        "Delivered"
    ]

    if order_id not in delivery_status:
        delivery_status[order_id] = 0

    current_stage = delivery_status[order_id]

    response = {
        "order_id": order_id,
        "status": stages[current_stage]
    }

    if current_stage < len(stages) - 1:
        delivery_status[order_id] += 1

    return response