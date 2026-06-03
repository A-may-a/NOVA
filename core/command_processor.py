from commands.app_commands import open_chrome
from commands.web_commands import open_google
from commands.system_commands import tell_time

def process(command):

    if command == "open google":
        open_google()
        return "Opening Google"

    elif command == "open chrome":
        open_chrome()
        return "Opening Chrome"

    elif command in ["what is the time", "tell time", "time"]:
        return f"The time is {tell_time()}"

    return None