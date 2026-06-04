import speech_recognition as sr

def listen():

    recognizer = sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening...")

        recognizer.adjust_for_ambient_noise(
            source,
            duration=1
        )

        audio = recognizer.listen(
            source,
            timeout=5,
            phrase_time_limit=5
        )

    try:

        command = recognizer.recognize_google(
            audio
        )

        print("Recognized:", command)

        return command.lower()

    except Exception as e:

        print("Speech Error:", e)

        return ""