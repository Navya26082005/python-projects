import random

faq = {
    "what is mca": "MCA is Master of Computer Applications.",
    "what is ai": "AI stands for Artificial Intelligence.",
    "who is your creator": "I am created by Navya.",
    "how are you": "I am fine, thank you!"
}

def chatbot():
    print("Hi! I am your AI Chatbot. Type 'quit' to exit.")
    while True:
        user_input = input("You: ").lower()
        if user_input == "quit":
            print("Chatbot: Goodbye!")
            break
        response = faq.get(user_input, "Sorry, I don't understand that.")
        print("Chatbot:", response)

chatbot()