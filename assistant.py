# assistant_text.py

def assistant():
    print("=== Welcome to Your AI Assistant ===")
    print("Type your command (type 'stop' to exit):")

    while True:
        command = input("You: ").lower()  # Get user input
        if "stop" in command:
            print("Assistant: Goodbye! 👋")
            break
        elif "hello" in command:
            print("Assistant: Hello! How are you?")
        elif "your name" in command:
            print("Assistant: I am your AI Assistant.")
        elif "time" in command:
            from datetime import datetime
            now = datetime.now().strftime("%H:%M:%S")
            print(f"Assistant: Current time is {now}")
        else:
            print("Assistant: Sorry, I can only answer simple questions like 'hello', 'time', or 'your name'.")

assistant()