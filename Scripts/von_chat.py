import cv2
import threading
import time
import pyttsx3

# Avatar Display Function
def show_avatar():
    img = cv2.imread("C:\\Users\\ASUS\\Downloads\\Coding Projects\\Project VON\\memory\\avatar.png")  # Make sure this file is in the same folder
    if img is None:
        print("Error: Could not load avatar image.")
        return
    cv2.imshow("Von Avatar", img)
    cv2.waitKey(0)  # Keeps window open until manually closed
    cv2.destroyAllWindows()

# 🗣️ TTS Engine Setup
engine = pyttsx3.init()
engine.setProperty('rate', 170)  # Speed of speech
engine.setProperty('volume', 1.0)  # Max volume

# 💬 Chat Function
def main_chat_loop():
    print("👋 Von: Hello! I'm listening.")
    while True:
        try:
            user_input = input("You: ")
            if user_input.lower() in ['exit', 'quit', 'bye']:
                print("Von: Goodbye!")
                engine.say("Goodbye!")
                engine.runAndWait()
                break

            # Placeholder AI logic — echo response
            response = f"I heard you say: {user_input}"
            print(f"Von: {response}")
            engine.say(response)
            engine.runAndWait()

        except KeyboardInterrupt:
            print("\nVon: See you later!")
            break

# 🚀 Start Avatar Display Thread
avatar_thread = threading.Thread(target=show_avatar)
avatar_thread.daemon = True  # Allows program to exit even if this is still running
avatar_thread.start()

# 🧠 Start Chat Loop
main_chat_loop()