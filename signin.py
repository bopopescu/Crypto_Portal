
import tkinter as tk
import extra_functions
from main_file import EntryWithPlaceholder


class SignIn(tk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent)
        # self.con.state("zoomed")
        self.columnconfigure(0, weight=1)

        canvas = tk.Canvas(self, bg="yellow green", bd=0)
        canvas.create_text(650, 140, text="Crypto Portal", anchor=tk.CENTER, font="Times 70 bold", fill="green")
        canvas.create_text(650, 140, text="Crypto Portal", anchor=tk.CENTER, font="Times 71 bold", fill="lime green")
        canvas.grid(row=0, column=0, sticky="NEWS", columnspan=10, rowspan=10)

        tk.Label(self).grid(row=0, column=0)
        self.rowconfigure(0, weight=10)

        self.default_font = font = tk.font.Font(family="Times", size=15)
        self.default_bg = "yellow green"

        self.username = tk.StringVar(self)
        username_entry = tk.Entry(self, bg=self.default_bg, font=self.default_font, textvariable=self.username,
                                  fg="green")
        username_entry.grid(row=1, column=0, ipady=10, pady=2, ipadx=40)
        self.rowconfigure(1, weight=1)
        EntryWithPlaceholder(username_entry, placeholder="Username")

        self.password = tk.StringVar(self)
        password_entry = tk.Entry(self, bg=self.default_bg, font=self.default_font, show="*",
                                  textvariable=self.password, fg="green")
        password_entry.grid(row=2, column=0, ipady=10, pady=2, ipadx=40)
        self.rowconfigure(2, weight=1)
        EntryWithPlaceholder(password_entry, placeholder="Password")

        self.messege = tk.StringVar()
        tk.Label(self, text="", textvariable=self.messege).grid(row=3, column=0)

        tk.Button(self, bg=self.default_bg, fg="blue", text="Login", font=self.default_font, bd=0,
                  command=self.do_login).grid(row=4, column=0, sticky="N", ipady=6, pady=(2))
        self.rowconfigure(3, weight=1)

        tk.Button(self, text="Forgot password?", bg=self.default_bg, bd=0, fg="red", font=self.default_font,
                  command=self.do_forgot_password).grid(row=5, column=0, sticky="N", ipadx=35, ipady=3)
        self.rowconfigure(4, weight=1)
        tk.Button(self, text="Back", font=self.default_font, fg="green", bg=self.default_bg, bd=3,
                  command=lambda: self.controller.show_frame("StartPage")).grid(row=6, column=0, sticky="S", ipadx=15,
                                                                                ipady=5, pady=(0, 100))
        self.rowconfigure(5, weight=1)

    def do_login(self):
        result = extra_functions.login_check( self.username.get(), self.password.get() )
        if result == "You have successfully logged in.":
            # login
            self.controller.show_frame("MainPage")
        else:
            self.messege.set( result )

    def do_forgot_password(self):
        print("do_forgot_password")
        self.controller.show_frame("MainPage")
