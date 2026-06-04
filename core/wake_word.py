
from core.speech import listen

WAKE_WORDS = [
    "hey nova",
    "nova",
    "hello nova"
]

def detect_wake_word():

    command = listen()

    if not command:
        return False

    for wake_word in WAKE_WORDS:
        if wake_word in command:
            return True

    return False