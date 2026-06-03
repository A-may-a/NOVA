from core.speech import listen
from core.tts import speak
from core.command_processor import process

speak("Nova Here!! How can I help you?")

while True:

    command = listen()

    if not command:
        continue

    print("You:", command)

    response = process(command)  # <-- Create response variable

    print("Response:", response)  # Debug

    if response:
        speak(response)
    else:
        speak("Command not recognized")