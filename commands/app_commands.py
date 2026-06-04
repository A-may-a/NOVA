import os

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

open_chrome()

def open_notepad():
    os.system("notepad")

def open_calculator():
    os.system("calc")

def open_paint():
    os.system("mspaint")

def open_vscode():
    os.startfile(
        r"C:\Users\ASUS\AppData\Local\Programs\Microsoft VS Code\Code.exe"
    )

def open_downloads():
    os.startfile(os.path.join(os.environ["USERPROFILE"], "Downloads"))

def open_documents():
    os.startfile(os.path.join(os.environ["USERPROFILE"], "Documents"))