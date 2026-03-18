import json
from data import ORDERS
from rag import search_policy, POLICY_CHUNKS

def lookup_order(order_id: str) -> str:
    order = ORDERS.get(order_id)
    if not order:
        return f"No order found with ID {order_id}."
    shipped = order["shipped_date"] or "Not yet shipped"
    cancel_status = "Yes" if order["can_cancel"] else "No, already shipped"

    return f"""
Order #{order["id"]} - {order["item"]}
Customer: {order["customer"]}
Status: {order["status"]}
Order Date: {order["order_date"]}
Shipped: {shipped}
Expected Delivery: {order["expected_delivery"]}
Amount: ₹{order["amount"]}
Can Cancel: {cancel_status}
""".strip()

def check_policy(topic: str) -> str:
    results = search_policy(topic, POLICY_CHUNKS)
    return "\n\n".join(results)

def cancel_order(order_id: str) -> str:
    order = ORDERS.get(order_id)
    if not order:
        return f"No order found with ID {order_id}."
    if not order["can_cancel"]:
        return f"Order #{order_id} cannot be cancelled as it has already been shipped."
    
    ORDERS[order_id]["status"] = "Cancelled"
    ORDERS[order_id]["can_cancel"] = False
    return f"Order #{order_id} has been cancelled successfully. Refund of ₹{order['amount']} will be processed within 5-7 business days."