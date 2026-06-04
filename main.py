from core.speech import listen
from core.tts import speak
from core.command_processor import process
from core.wake_word import detect_wake_word

speak("Nova Activated")

while True:

    print("Waiting for wake word...")

    if detect_wake_word():

        speak("Yes?")
        command = listen()

    if not command:
        continue

    print("You:", command)

    response = process(command)

    if response == "EXIT":
        speak("Goodbye")
        break

    elif response:
        speak(response)

    else:
        speak("Command not recognized")