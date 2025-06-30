import json
from datetime import datetime
import os

# === CONFIG ===
MEMORY_PATH = "../memory/project_von_memory.json"

# === Load memory ===
def load_memory():
    with open(MEMORY_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

# === Save updated memory ===
def save_memory(data):
    with open(MEMORY_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

# === Generate a simple reply (MVP placeholder) ===
def generate_reply(user_input):
    if "hello" in user_input.lower():
        return "Hi! I'm Von. How can I help you today?"
    elif "lazy" in user_input.lower():
        return "Let’s try setting a tiny goal together."
    elif "bye" in user_input.lower():
        return "Goodbye. Take care of yourself. 🌱"
    else:
        return "Hmm, I’m still learning. Tell me more."

# === Add message to memory ===
def append_message(memory, role, text):
    new_msg = {
        "role": role,
        "content": text,
        "timestamp": datetime.utcnow().isoformat() + "Z"
    }
    memory["sessionContext"]["messages"].append(new_msg)

# === MAIN LOOP ===
def chat_loop():
    print("🧠 Von: Hello, I’m Von. Your personal AI memory.\n(Type 'bye' to exit.)")

    memory = load_memory()

    while True:
        user_input = input("> You: ").strip()
        if not user_input:
            continue

        append_message(memory, "user", user_input)

        if user_input.lower() == "bye":
            von_reply = "Goodbye. Take care of yourself. 🌱"
            print(f"Von: {von_reply}")
            append_message(memory, "von", von_reply)
            break

        von_reply = generate_reply(user_input)
        print(f"Von: {von_reply}")
        append_message(memory, "von", von_reply)

    save_memory(memory)
    print("✅ Session saved to memory.")

if __name__ == "__main__":
    chat_loop()
