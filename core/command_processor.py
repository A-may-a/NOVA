from commands.app_commands import *
from commands.web_commands import *
from commands.system_commands import *
from commands.fun_commands import *

def process(command):

    command = command.lower()

    # Apps
    if "open chrome" in command:
        open_chrome()
        return "Opening Chrome"

    elif "open notepad" in command:
        open_notepad()
        return "Opening Notepad"

    elif "open calculator" in command:
        open_calculator()
        return "Opening Calculator"

    elif "open paint" in command:
        open_paint()
        return "Opening Paint"

    elif "open vscode" in command or "open vs code" in command:
        open_vscode()
        return "Opening VS Code"

    elif "open downloads" in command:
        open_downloads()
        return "Opening Downloads"

    elif "open documents" in command:
        open_documents()
        return "Opening Documents"

    # Websites
    elif "open google" in command:
        open_google()
        return "Opening Google"

    elif "open youtube" in command:
        open_youtube()
        return "Opening YouTube"

    elif "open github" in command:
        open_github()
        return "Opening GitHub"

    elif "open chatgpt" in command:
        open_chatgpt()
        return "Opening ChatGPT"

    # Time & Date
    elif "time" in command:
        return f"The time is {tell_time()}"

    elif "date" in command:
        return f"Today's date is {tell_date()}"

    elif "day" in command:
        return f"Today is {tell_day()}"

    # Fun
    elif "who are you" in command:
        return who_are_you()

    elif "how are you" in command or "how r u" in command:
        return how_are_you()

    elif "joke" in command:
        return tell_joke()

    # Exit
    elif "exit nova" in command or "stop nova" in command or "exit" in command or "stop" in command:
        return "EXIT"

    return None