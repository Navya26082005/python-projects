# full_ai_assistant.py

import datetime
import webbrowser
import wikipedia

# Assistant greeting
def greet():
    print("=== Welcome to Your AI Assistant ===")
    print("Type your command (type 'stop' to exit)\n")

# Main assistant function
def assistant():
    greet()
    while True:
        command = input("You: ").lower()

        # Exit the assistant
        if "stop" in command or "exit" in command:
            print("Assistant: Goodbye! 👋")
            break

        # Basic greetings
        elif "hello" in command or "hi" in command:
            print("Assistant: Hello! How are you?")
        elif "your name" in command:
            print("Assistant: I am your AI Assistant.")

        # Time & date
        elif "time" in command:
            now = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"Assistant: Current time is {now}")
        elif "date" in command:
            today = datetime.datetime.now().strftime("%Y-%m-%d")
            print(f"Assistant: Today's date is {today}")

        # Open websites
        elif "open youtube" in command:
            print("Assistant: Opening YouTube...")
            webbrowser.open("https://www.youtube.com")
        elif "open google" in command:
            print("Assistant: Opening Google...")
            webbrowser.open("https://www.google.com")

        # Wikipedia search
        elif "search wikipedia" in command:
            try:
                topic = command.replace("search wikipedia", "").strip()
                if topic == "":
                    topic = input("Assistant: What should I search for? ")
                result = wikipedia.summary(topic, sentences=2)
                print("Assistant (Wikipedia):", result)
            except Exception as e:
                print("Assistant: Sorry, I couldn't find that.")

        # Simple unknown command handler
        else:
            print("Assistant: Sorry, I can respond to greetings, time, date, Wikipedia search, or open websites.")

# Run the assistant
if __name__ == "__main__":
    assistant()