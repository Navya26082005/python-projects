import random

print("Simple AI Text Generator")

topic = input("Enter a topic: ")

sentences = [
    f"{topic} is a very interesting concept in modern science.",
    f"Many researchers are studying {topic} to improve technology.",
    f"{topic} plays an important role in our daily life.",
    f"In the future, {topic} will become even more important.",
    f"Students and scientists are learning more about {topic} every day."
]

print("\nGenerated Paragraph:\n")

for i in range(3):
    print(random.choice(sentences))