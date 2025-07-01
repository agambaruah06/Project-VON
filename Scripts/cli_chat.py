import os

def load_system_prompt():
    with open("C:\\Users\\ASUS\\Downloads\\Coding Projects\\Project VON\\prompts\\system_prompt.txt", encoding="utf-8") as f:
        return f.read()

system_prompt = load_system_prompt()

import json
from datetime import datetime, timezone
from tts_utils import speak_text


# === CONFIG ===
MEMORY_PATH = "C:\\Users\\ASUS\\Downloads\\Coding Projects\\Project VON\\memory\\project_von_memory.json"

# === Load memory ===
def load_memory():
    with open(MEMORY_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

# === Save updated memory ===
def save_memory(data):
    with open(MEMORY_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

import random

def generate_reply(user_input, memory, system_prompt):
    # Totally offline: local canned responses
    offline_responses = [
        "I see. Tell me more about why you feel that way.",
        "Interesting—what would your best self do here?",
        "Let’s try to plan a tiny next step together.",
        "That’s honest. How can we make progress on this?",
        "Sounds tricky. What do you think would really help?"
    ]

    # A simple bit of 'smartness'
    if "lazy" in user_input.lower():
        return "Feeling unmotivated is normal. Let's pick one tiny goal to start."
    if "plan" in user_input.lower():
        return "Sure, let’s plan it step by step. What’s the outcome you want?"
    if "bye" in user_input.lower():
        return "Goodbye. Take care of yourself. 🌱"
    if "help" in user_input.lower():
        return "I’m always here to help you clarify your goals."

    # Otherwise random canned coaching-style reply
    return random.choice(offline_responses)


# === Add message to memory ===
def append_message(memory, role, text):
    new_msg = {
        "role": role,
        "content": text,
        "timestamp": datetime.now(timezone.utc).isoformat()
    }
    memory["sessionContext"]["messages"].append(new_msg)

# === MAIN LOOP ===
def chat_loop():
    print("🧠 Von: Hello, I’m Von. Your personal AI memory.\n(Type 'bye' to exit.)")
    speak_text('Hello, I’m Von. Your personal AI memory.')


    memory = load_memory()

    while True:
        user_input = input("> You: ").strip()
        if not user_input:
            continue

        append_message(memory, "user", user_input)

        if user_input.lower() == "bye":
            von_reply = "Goodbye. Take care of yourself. 🌱"
            print(f"Von: {von_reply}")
            speak_text(von_reply)
            append_message(memory, "von", von_reply)
            break

        von_reply = generate_reply(user_input, memory, system_prompt)
        print(f"Von: {von_reply}")
        speak_text(von_reply)
        append_message(memory, "von", von_reply)

    save_memory(memory)
    print("✅ Session saved to memory.")
    speak_text("Session saved to memory.")

if __name__ == "__main__":
    chat_loop()
