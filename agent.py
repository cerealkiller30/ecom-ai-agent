import os
import json
from groq import Groq
from tools import lookup_order, check_policy, cancel_order

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
MODEL = "llama-3.3-70b-versatile"

TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "lookup_order",
            "description": "Look up the status, shipping info, and details of a customer order using the order ID.",
            "parameters": {
                "type": "object",
                "properties": {
                    "order_id": {
                        "type": "string",
                        "description": "The order ID number, e.g. '1234'"
                    }
                },
                "required": ["order_id"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "check_policy",
            "description": "Search the store policy for information about returns, refunds, cancellations, shipping, or damaged items.",
            "parameters": {
                "type": "object",
                "properties": {
                    "topic": {
                        "type": "string",
                        "description": "The policy topic to search for, e.g. 'return policy'"
                    }
                },
                "required": ["topic"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "cancel_order",
            "description": "Cancel a customer order. Only works if the order has not shipped yet.",
            "parameters": {
                "type": "object",
                "properties": {
                    "order_id": {
                        "type": "string",
                        "description": "The order ID to cancel"
                    }
                },
                "required": ["order_id"]
            }
        }
    }
]

SYSTEM_PROMPT = """You are a friendly and helpful customer support agent for ShopEasy,
an Indian e-commerce platform.

You have access to three tools:
- lookup_order: to find order details
- check_policy: to answer questions about returns, shipping, cancellations
- cancel_order: to cancel an order on the customer's request

Always use a tool before answering — never guess order details or policy rules.
Be warm, concise, and helpful. If a customer seems frustrated, acknowledge it.
Always mention the order item name (not just the ID) when referring to an order."""


def run_tool(name: str, arguments: dict) -> str:
    if name == "lookup_order":
        return lookup_order(arguments["order_id"])
    elif name == "check_policy":
        return check_policy(arguments["topic"])
    elif name == "cancel_order":
        return cancel_order(arguments["order_id"])
    return "Unknown tool."


def chat(conversation_history: list, user_message: str) -> str:
    conversation_history.append({
        "role": "user",
        "content": user_message
    })
    while True:
        response = client.chat.completions.create(
            model=MODEL,
            messages=[{"role": "system", "content": SYSTEM_PROMPT}] + conversation_history,
            tools=TOOLS,
            tool_choice="auto",
            max_tokens=1024
        )

        message = response.choices[0].message

        if message.tool_calls:
            conversation_history.append({
                "role": "assistant",
                "content": message.content,
                "tool_calls": message.tool_calls
            })

            for tool_call in message.tool_calls:
                print(f"  [calling {tool_call.function.name}...]")
                arguments = json.loads(tool_call.function.arguments)
                result = run_tool(tool_call.function.name, arguments)

                conversation_history.append({
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": result
                })

        else:
            reply = message.content
            conversation_history.append({
                "role": "assistant",
                "content": reply
            })

            return reply
