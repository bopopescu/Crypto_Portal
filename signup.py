
import tkinter as tk
import extra_functions
import database


class SignUp(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.default_font = font = tk.font.Font(family="Times", size=15)
        self.default_bg = "yellow green"
        self.default_fg = "green"

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        canvas = tk.Canvas(self, bg=self.default_bg, bd=0)
        canvas.create_text(650, 110, text="Crypto Portal", anchor=tk.CENTER, font="Times 70 bold", fill="green")
        canvas.create_text(650, 110, text="Crypto Portal", anchor=tk.CENTER, font="Times 71 bold", fill="lime green")
        canvas.grid(row=0, column=0, sticky="NEWS", columnspan=20, rowspan=20)
        self.rowconfigure(0, weight=7)

        """Adding the labels required fields for the sign up page"""
        tk.Label(self, text="Username", font=self.default_font, fg=self.default_fg, bg=self.default_bg).grid(column=0,row=1,sticky="E")
        tk.Label(self, text="Phone", font=self.default_font, fg=self.default_fg, bg=self.default_bg).grid(column=0, row=2,sticky="E")
        tk.Label(self, text="Email", font=self.default_font, fg=self.default_fg, bg=self.default_bg).grid(column=0,row=3, sticky="E")
        tk.Label(self, text="Password", font=self.default_font, fg=self.default_fg, bg=self.default_bg).grid(column=0,row=4, sticky="E")
        tk.Label(self, text="Re-enter password", font=self.default_font, fg=self.default_fg, bg=self.default_bg).grid(column=0, row=5, sticky="E")

        for i in range(1, 6):
            self.rowconfigure(i, weight=1)

        """Creating entry fields and variables which will store data from the entry fields"""

        self.username = tk.StringVar()
        name_ent = tk.Entry(self, textvariable=self.username, bg=self.default_bg, font=self.default_font)
        name_ent.grid(column=1, row=1, sticky="W")

        self.phone = tk.StringVar()
        phone_ent = tk.Entry(self, textvariable=self.phone, bg=self.default_bg, font=self.default_font)
        phone_ent.grid(column=1, row=2, sticky="W")

        self.email = tk.StringVar()
        email_ent = tk.Entry(self, textvariable=self.email, bg=self.default_bg, font=self.default_font)
        email_ent.grid(column=1, row=3, sticky="W")

        self.password = tk.StringVar()
        password_ent = tk.Entry(self, show="*", textvariable=self.password, bg=self.default_bg, font=self.default_font)
        password_ent.grid(column=1, row=4, sticky="W")

        self.password2 = tk.StringVar()
        password2_ent = tk.Entry(self, show="*", textvariable=self.password2, bg=self.default_bg, font=self.default_font)
        password2_ent.grid(column=1, row=5, sticky="W", pady=(13, 0))

        create_profile_btn = tk.Button(self, bg=self.default_bg, fg="green", text="Create profile",command=self.click_create_profile, font=self.default_font)
        create_profile_btn.grid(column=0, columnspan=2, row=6, pady=(15, 0), ipadx=10, ipady=4)

        back_btn = tk.Button(self, bg=self.default_bg, fg="green", text="Back",command=lambda: controller.show_frame("StartPage"), font=self.default_font)
        back_btn.grid(column=1, row=7)

        self.test = tk.Label(self, text="Please complete your profile.", bg=self.default_bg, fg="green")
        self.test.grid(column=1, row=8, pady=(0, 70))

    # Button for the create profile button if successful it will take you to the MainPage else a error message will pop up
    def click_create_profile(self):
        username = self.username.get()
        phone = self.phone.get()
        email = self.email.get()
        password = self.password.get()
        password2 = self.password2.get()
        return_message = extra_functions.details_check(username, email, phone, password, password2)
        if return_message == "Account created!":
            database.create_user(username=username, password=password, email=email, phone=phone)
            self.controller.show_frame("MainPage")
        else:
            self.test.configure(text=return_message)


    def update(self):
        nothing= "nothing"
