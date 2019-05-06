import tkinter as tk


# The page where our wallets will be created
class Wallets(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.options_frame = tk.Frame(self)
        self.options_frame.grid(column="0", columnspan="2", row="0")

        main_page = tk.Button(self.options_frame, text="Main Page", command=lambda: controller.show_frame("MainPage"))
        main_page.grid(column="0", columnspan="2", row="0")

        log_out = tk.Button(self.options_frame, text="Logout", command=lambda: self.controller.show_frame("StartPage"))
        log_out.grid(column="3", row="0")

