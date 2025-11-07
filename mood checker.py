import random

def simple_mood_checker():
    print("🎯 Welcome to the Simple Mood Checker Game! 🎯")
    print("Type anything — your name, a random word, or how you feel right now — and I’ll tell you your mood for today! 😄")
    print("\nReady? Let’s check your mood...")

    user_input = input("Type something and press Enter! ✨ ")

    moods = [
        "joyful! 😊",
        "calm. 😌",
        "energetic! ⚡",
        "thoughtful. 🤔",
        "optimistic! ✨",
        "peaceful. 🧘‍♀️",
        "curious. 🧐",
        "content. 😊",
        "inspired! 💡",
        "relaxed. ☕"
    ]

    selected_mood = random.choice(moods)
    print(f"\nIt seems you are feeling {selected_mood}")
    print("\nThanks for playing! 👋")

if __name__ == "__main__":
    simple_mood_checker()