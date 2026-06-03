import os

def open_chrome():
    paths = [
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
        rf"C:\Users\{os.getlogin()}\AppData\Local\Google\Chrome\Application\chrome.exe"
    ]

    for path in paths:
        if os.path.exists(path):
            os.startfile(path)
            return

    print("Chrome not found!")

#open_chrome()