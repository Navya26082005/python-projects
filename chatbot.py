print("Hello! I am Navya's AI Chatbot 🤖")
print("You can ask me things like:")
print("hello, your name, what is ai, who created you")
print("Type 'bye' to exit.\n")

while True:
    user = input("You: ").lower()

    if "hello" in user:
        print("Bot: Hello! Nice to meet you.")

    elif "name" in user:
        print("Bot: I am Navya's Python Chatbot.")

    elif "ai" in user:
        print("Bot: AI means Artificial Intelligence.")

    elif "who created you" in user:
        print("Bot: I was created by Navya using Python.")

    elif "bye" in user:
        print("Bot: Goodbye! Have a great day.")
        break

    else:
        print("Bot: Sorry, I don't understand that yet.")