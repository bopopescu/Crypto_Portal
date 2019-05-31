import tkinter as tk

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.default_bg = "yellow green"

        self.columnconfigure(0, weight=1)

        canvas = tk.Canvas(self, bg=self.default_bg, bd=0)
        canvas.create_text(650, 140, text="Crypto Portal", anchor=tk.CENTER, font="Times 70 bold", fill="green")
        canvas.create_text(650, 140, text="Crypto Portal", anchor=tk.CENTER, font="Times 71 bold", fill="lime green")
        canvas.grid(row=0, column=0, sticky="NEWS", columnspan=10, rowspan=10)

        self.rowconfigure(0, weight=3)

        button_font = tk.font.Font(family="Times", size=13)

        button1 = tk.Button(self, text="Sign in", bg=self.default_bg, fg="green", font=button_font,
                            command=lambda: controller.show_frame("SignIn"))
        button1.grid(row=1, column=0, ipadx=30, ipady=8)
        self.rowconfigure(1, weight=1)

        button2 = tk.Button(self, text="Sign up", fg="green", bg=self.default_bg, font=button_font,
                            command=lambda: controller.show_frame("SignUp"))
        button2.grid(row=2, column=0, ipadx=30, ipady=10, sticky="N", pady=(0, 100))
        self.rowconfigure(2, weight=1)

    def update_page(self):
        nothing="nothing"
