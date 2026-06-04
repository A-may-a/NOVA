from gui.main_window import NovaGUI

app = NovaGUI()

app.add_user_message("Open Chrome")

app.add_assistant_message("Opening Chrome")

app.update_status("Listening")

app.run()