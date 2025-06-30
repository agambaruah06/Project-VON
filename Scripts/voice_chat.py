import speech_recognition as sr
import pyttsx3
import json
import os

# Setup paths
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
MEMORY_PATH = os.path.join(SCRIPT_DIR, "..", "memory", "project_von_memory.json")

# Text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 175)

def speak(text):
    print(f"🧠 Von: {text}")
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎙️ Listening...")
        audio = recognizer.listen(source)

    try:
        return recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that.")
        return ""
    except sr.RequestError:
        speak("Speech service is unavailable.")
        return ""

def load_memory():
    with open(MEMORY_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def generate_reply(prompt):
    # Simple echo logic for now
    return f"You said: {prompt}"

def chat_loop():
    speak("Hello. I’m Von. Your voice AI memory.")
    memory = load_memory()

    while True:
        query = listen()
        if query.lower() in ["bye", "exit", "quit"]:
            speak("Goodbye.")
            break
        response = generate_reply(query)
        speak(response)

if __name__ == "__main__":
    chat_loop()