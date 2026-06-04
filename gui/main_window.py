import customtkinter as ctk

class NovaGUI:

    def __init__(self):

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.root = ctk.CTk()

        self.root.title("NOVA Assistant")

        self.root.geometry("700x500")

        self.root.resizable(False, False)

        self.create_widgets()

    def create_widgets(self):

        # Title
        self.title_label = ctk.CTkLabel(
            self.root,
            text="NOVA",
            font=("Arial", 30, "bold")
        )

        self.title_label.pack(pady=20)

        # Status
        self.status_label = ctk.CTkLabel(
            self.root,
            text="Status: Ready",
            font=("Arial", 16)
        )

        self.status_label.pack(pady=10)

        # Conversation Box
        self.chat_box = ctk.CTkTextbox(
            self.root,
            width=600,
            height=250
        )

        self.chat_box.pack(pady=20)

        # Listen Button
        self.listen_button = ctk.CTkButton(
        self.root,
        text="🎤 Start Listening",
        command=self.test_button
         )

        self.listen_button.pack(pady=20)
    
    def add_user_message(self, message):

        self.chat_box.insert(
        "end",
        f"\n🧑 You: {message}\n"
        )

    def add_assistant_message(self, message):

        self.chat_box.insert(
        "end",
        f"🤖 Nova: {message}\n"
        )

    def update_status(self, status):

        self.status_label.configure(
        text=f"Status: {status}"
        )

    def test_button(self):

     self.update_status("Listening")

     self.add_user_message("Hello Nova")

     self.add_assistant_message("How can I help you?")

    def run(self):
        self.root.mainloop()