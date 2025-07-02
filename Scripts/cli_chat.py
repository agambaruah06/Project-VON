import os
import json
import random
from datetime import datetime, timezone
import ollama
# Replace tts_utils with pyttsx3 or create your own
import pyttsx3

# === CONFIG ===
MEMORY_PATH = "C:\\Users\\ASUS\\Downloads\\Coding Projects\\Project-VON\\memory\\project_von_memory.json"

# === TTS Function ===
def speak_text(text):
    try:
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print(f"TTS Error: {e}")

# === Load system prompt ===
def load_system_prompt():
    with open(
        "C:\\Users\\ASUS\\Downloads\\Coding Projects\\Project-VON\\prompts\\system_prompt.txt",
        encoding="utf-8"
    ) as f:
        return f.read()

system_prompt = load_system_prompt()

# === Load memory ===
def load_memory():
    if not os.path.exists(MEMORY_PATH):
        return {"sessionContext": {"messages": []}}
    with open(MEMORY_PATH, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            print("⚠️ Memory file is corrupted. Starting fresh.")
            return {"sessionContext": {"messages": []}}

# === Save updated memory ===
def save_memory(data):
    with open(MEMORY_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

# === Generate reply using Ollama locally ===
def generate_reply(user_input, memory, system_prompt):
    try:
        messages = [{"role": "system", "content": system_prompt}]
        
        # Include last 4 messages as context
        session_msgs = memory.get("sessionContext", {}).get("messages", [])
        if session_msgs:
            messages.extend(session_msgs[-4:])

        messages.append({"role": "user", "content": user_input})

        # Optional debug
        print("\n[Debug] Sending to model:\n", json.dumps(messages, indent=2, ensure_ascii=False))

        response = ollama.chat(
            model='phi',
            messages=messages
        )

        print("[Debug] Model reply received\n")
        return response['message']['content'].strip()
        
    except Exception as e:
        print(f"Error generating reply: {e}")
        return "I'm having trouble processing your request right now."

# === Append message to memory ===
def append_message(memory, role, text):
    if "sessionContext" not in memory:
        memory["sessionContext"] = {"messages": []}
    new_msg = {
        "role": role,
        "content": text,
        "timestamp": datetime.now(timezone.utc).isoformat()
    }
    memory["sessionContext"]["messages"].append(new_msg)

# === MAIN LOOP ===
def chat_loop():
    print("🧠 Von: Hello, I'm Von. Your personal AI memory.\n(Type 'bye' to exit, or 'reset' to clear memory.)")
    speak_text("Hello, I'm Von. Your personal AI memory.")

    memory = load_memory()

    while True:
        user_input = input("> You: ").strip()
        if not user_input:
            continue

        # Handle reset
        if user_input.lower() == "reset":
            memory["sessionContext"]["messages"] = []
            print("🔄 Memory reset.")
            speak_text("Memory reset.")
            continue

        # Handle exit
        if user_input.lower() == "bye":
            von_reply = "Goodbye. Take care of yourself. 🌱"
            print(f"Von: {von_reply}")
            speak_text(von_reply)
            append_message(memory, "von", von_reply)
            break

        # Normal flow
        append_message(memory, "user", user_input)
        von_reply = generate_reply(user_input, memory, system_prompt)
        print(f"Von: {von_reply}")
        speak_text(von_reply)
        append_message(memory, "von", von_reply)

    save_memory(memory)
    print("✅ Session saved to memory.")
    speak_text("Session saved to memory.")

if __name__ == "__main__":
    chat_loop()
