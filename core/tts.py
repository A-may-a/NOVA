import threading
import pyttsx3

def speak(text):

    def run():

        engine = pyttsx3.init()

        engine.say(text)

        engine.runAndWait()

    threading.Thread(
        target=run,
        daemon=True
    ).start()