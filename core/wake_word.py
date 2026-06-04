
from core.speech import listen

WAKE_WORDS = [
    "hey nova",
    "nova",
    "hello nova"
    "hey noah"
]

def detect_wake_word():

    command = listen()

    print("Wake heard:", command)

    if not command:
        return False

    command = command.lower()

    for wake_word in WAKE_WORDS:

        if wake_word in command:

            print("Wake word matched")

            return True

    return False