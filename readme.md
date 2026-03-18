# E-commerce Customer Support Agent

An AI-powered customer support agent for e-commerce platforms, built using
Agentic AI and RAG (Retrieval-Augmented Generation) architecture.

## What it does

A customer can chat in plain English and the agent will:
- Track any order by ID
- Answer questions about return, refund, and shipping policy
- Cancel eligible orders automatically

The agent decides which action to take on its own — no hardcoded if/else logic.

## Architecture
```
User Query
    ↓
LLM Agent (Llama 3.3 via Groq)
    ↓ decides which tool to call
    ├── lookup_order   → searches order database
    ├── check_policy   → RAG search on policy document
    └── cancel_order   → updates order status
    ↓
Natural language response
```

## Tech Stack

- **LLM:** Llama 3.3 70B (via Groq API)
- **Agentic Pattern:** Tool use / function calling
- **RAG:** Keyword-based policy document retrieval
- **Language:** Python 3.x

## Setup

1. Clone the repo
```bash
   git clone https://github.com/cerealkiller30/ecom-ai-agent.git
   cd ecom-ai-agent
```

2. Create and activate virtual environment
```bash
   python -m venv venv
   venv\Scripts\activate
```

3. Install dependencies
```bash
   pip install -r requirements.txt
```

4. Set your Groq API key
```bash
   # Windows PowerShell
   $env:GROQ_API_KEY="your_key_here"
```

5. Run the agent
```bash
   python app.py
```

## Sample Conversation
```
Agent: Hi! Welcome. How can I help you?

You: cancel order 1234
Agent: I understand that you're trying to cancel your order for the Blue Adidas Sneakers (#1234), but unfortunately, it has already been shipped and is out for delivery. I've checked the status, and it's expected to be delivered today. If you'd like to return or exchange it after receiving the order, I can help you with that process. Would you like to know more about our return policy?

You: No. give me details about this order.
Agent: The details of your order #1234 for the Blue Adidas Sneakers are as follows:

- Customer Name: Arjun Sharma
- Order Status: Out for Delivery
- Order Date: 13 March, 2026
- Shipped: 15 March, 2026
- Expected Delivery: 18 March, 2026
- Total Amount: ₹2499

If you have any other questions or need further assistance, please let me know.

You: cancel order 5678
Agent: Your order #5678 for the Sony Wireless Headphones has been cancelled successfully. You will receive a refund of ₹4999 within 5-7 business days. If you have any other questions or need further assistance, please let me know.

You: Ok bye.
Agent: It was a pleasure assisting you. Have a great day and feel free to reach out if you need anything else. Bye!
```

## Concepts Demonstrated

| Concept | Where |
|---|---|
| Agentic AI | `agent.py` — autonomous tool selection loop |
| RAG | `rag.py` — policy document retrieval |
| Tool Use | `tools.py` — three callable functions |
| Multi-turn Memory | `agent.py` — conversation history |
| GenAI Integration | `agent.py` — LLM API call |

## Future Improvements

- Implement semantic RAG (vector embedding)
- Connect to a real database instead of mock data
- Add a web UI using Flask
