from dotenv import load_dotenv
load_dotenv()
from agent import chat

def main():
    print(" Customer Support Agent (type 'quit' to exit)")
    print("="*30)
    print("\nAgent: Hi! Welcome. How can I help you?\n")

    conversation_history = []

    while True:
        user_input = input("You: ").strip()

        if not user_input:
            continue
        if user_input.lower() in ["quit", "exit", "bye"]:
            print("Agent: Goodbye! Have a great day!")
            break

        reply = chat(conversation_history, user_input)
        print(f"Agent: {reply}\n")

if __name__ == "__main__":
    main()