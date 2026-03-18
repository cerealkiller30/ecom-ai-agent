# Mock database for practice project

ORDERS = {
    "1234": {
        "id": "1234",
        "customer": "Arjun Sharma",
        "item": "Blue Adidas Sneakers",
        "status": "Out for Delivery",
        "order_date": "13 March, 2026",
        "shipped_date": "15 March, 2026",
        "expected_delivery": "18 March, 2026",
        "amount": 2499,
        "can_cancel": False  
    },
    "5678": {
        "id": "5678",
        "customer": "Rahul Singh",
        "item": "Sony Wireless Headphones",
        "status": "Processing",
        "order_date": "17 March, 2026",
        "shipped_date": None,
        "expected_delivery": "22 March, 2026",
        "amount": 4999,
        "can_cancel": True   
    },
    "9999": {
        "id": "9999",
        "customer": "Pooja Mehta",
        "item": "Cotton Kurta Set",
        "status": "Delivered",
        "order_date": "13 March, 2026",
        "shipped_date": "15 March, 2026",
        "expected_delivery": "18 March, 2026",
        "amount": 899,
        "can_cancel": False
    }
}