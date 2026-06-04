import customtkinter as ctk
import threading

from core.speech import listen
from core.tts import speak
from core.command_processor import process
from core.wake_word import detect_wake_word

class NovaGUI:

    def __init__(self):

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.root = ctk.CTk()

        self.root.title("NOVA Assistant")
        self.root.geometry("800x600")
        self.root.resizable(False, False)

        self.create_widgets()

        threading.Thread(target=self.wake_word_loop,daemon=True).start()

    def create_widgets(self):

        # Logo
        self.logo_label = ctk.CTkLabel(
            self.root,
            text="⚡",
            font=("Segoe UI", 50)
        )

        self.logo_label.pack(pady=(20, 5))

        # Title
        self.title_label = ctk.CTkLabel(
            self.root,
            text="🤖 NOVA",
            font=("Segoe UI", 32, "bold")
        )

        self.title_label.pack(pady=5)

        # Status
        self.status_label = ctk.CTkLabel(
            self.root,
            text="🟢 Ready",
            font=("Segoe UI", 16)
        )

        self.status_label.pack(pady=5)

        # Mic Status
        self.mic_label = ctk.CTkLabel(
            self.root,
            text="🎤 Idle",
            font=("Segoe UI", 14)
        )

        self.mic_label.pack(pady=5)

        # Chat Box
        self.chat_box = ctk.CTkTextbox(
            self.root,
            width=700,
            height=320,
            font=("Segoe UI", 14)
        )

        self.chat_box.pack(pady=15)

        self.chat_box.configure(state="disabled")

        # Welcome Message
        self.add_assistant_message(
            "Nova online. How can I help you?"
        )

        # Listen Button
        self.listen_button = ctk.CTkButton(
            self.root,
            text="🎤 Start Listening",
            width=220,
            height=50,
            font=("Segoe UI", 16, "bold"),
            command=self.start_listening
        )

        self.listen_button.pack(pady=20)

    def add_user_message(self, message):

        self.chat_box.configure(state="normal")

        self.chat_box.insert(
            "end",
            f"\n🧑 You: {message}\n"
        )

        self.chat_box.see("end")

        self.chat_box.configure(state="disabled")

    def add_assistant_message(self, message):

        self.chat_box.configure(state="normal")

        self.chat_box.insert(
            "end",
            f"🤖 Nova: {message}\n"
        )

        self.chat_box.see("end")

        self.chat_box.configure(state="disabled")

    def update_status(self, status):

        if status == "Listening":

            self.status_label.configure(
                text="🔴 Listening..."
            )

            self.mic_label.configure(
                text="🎤 Active"
            )

        elif status == "Thinking":

            self.status_label.configure(
                text="🟡 Processing..."
            )

            self.mic_label.configure(
                text="🎤 Active"
            )

        else:

            self.status_label.configure(
                text="🟢 Ready for Wake Word."
            )

            self.mic_label.configure(
                text="🎤 Idle"
            )

    def start_listening(self):

        self.listen_button.configure(
            state="disabled"
        )

        thread = threading.Thread(
            target=self.listen_and_process
        )

        thread.daemon = True

        thread.start()

    def listen_and_process(self):

        try:

            self.update_status("Listening")

            command = listen()

            print("Recognized command:", command)

            if not command:

                return

            self.add_user_message(command)

            self.update_status("Thinking")

            response = process(command)

            if response:

                self.add_assistant_message(
                    response
                )

                speak(response)

            else:

                self.add_assistant_message(
                    "Command not recognized"
                )

                speak(
                    "Command not recognized"
                )

        except Exception as e:

            error_message = f"Error: {e}"

            self.add_assistant_message(
                error_message
            )

            print(error_message)

        finally:

            self.update_status("Ready")

            self.listen_button.configure(
                state="normal"
            )

    def wake_word_loop(self):

     while True:

        try:

            print("=== WAITING FOR WAKE WORD ===")

            self.status_label.configure(
                text="🟢 Waiting for Wake Word"
            )

            self.mic_label.configure(
                text="🎤 Passive"
            )

            if detect_wake_word():

                print("WAKE WORD DETECTED")

                self.add_assistant_message(
                    "Wake word detected"
                )

                speak("Yes?")

                self.status_label.configure(
                    text="🔴 Listening..."
                )

                self.mic_label.configure(
                    text="🎤 Active"
                )

                print("LISTENING FOR COMMAND")

                command = listen()

                print("COMMAND:", command)

                if not command:

                    self.add_assistant_message(
                        "I didn't hear anything."
                    )

                    continue

                self.add_user_message(command)

                self.status_label.configure(
                    text="🟡 Processing..."
                )

                response = process(command)

                print("RESPONSE:", response)

                if response == "EXIT":

                 self.add_assistant_message("Goodbye")

                 speak("Goodbye")

                 self.root.quit()

                 return

                elif response:

                 self.add_assistant_message(response)

                 speak(response)

                else:

                 self.add_assistant_message("Command not recognized")

                 speak("Command not recognized" )

                print("RETURNING TO WAKE WORD MODE"  )

        except Exception as e:

            print("Wake Word Error:", e)

            self.add_assistant_message(
                f"Error: {e}"
            )
    def run(self):

        self.root.mainloop()