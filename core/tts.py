import pyttsx3

def speak(text):
    engine = pyttsx3.init()

    print("Assistant:", text)

    engine.say(text)
    engine.runAndWait()

    engine.stop()