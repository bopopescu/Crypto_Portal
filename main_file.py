import tkinter as tk                # python 3
from tkinter import font  as tkfont # python 3
from extra_functions import details_check


class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Crypto-Portal")

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        self.labels_font = tkfont.Font(family='Helvetica', size=14, weight="bold", slant="italic")
        self.padding = ""

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, SignIn, SignUp):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is the start page", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Sign in", padx=10, pady=10,
                            command=lambda: controller.show_frame("SignIn"))
        button2 = tk.Button(self, text="Sign up", padx=10, pady=10,
                            command=lambda: controller.show_frame("SignUp"))
        button1.pack()
        button2.pack()


class SignIn(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="black")
        tk.Frame.config(self, width="500", height="500")
        self.controller = controller

        title_frame = tk.Frame(self, bg="lawn green")
        title_frame.place(relx=0, rely=0, relwidth=1, relheight=1 / 3)
        credits_frame = tk.Frame(self, bg="lawn green")
        credits_frame.place(relx=0, rely=1 / 3, relwidth=1, relheight=1 / 3)
        login_frame = tk.Frame(self, bg="lawn green")
        login_frame.place(relx=0, rely=2 / 3, relwidth=1, relheight=1 / 3)

        title_label = tk.Label(title_frame, bg="lawn green", text="Crypto Portal", font=controller.title_font).pack(
            side="top", fill="x", pady=10)
        login_label = tk.Label(title_frame, text="Login", bg="lime green").pack()

        self.username = tk.StringVar()
        self.password = tk.StringVar()

        credits_container = tk.Frame(credits_frame, bg="lawn green")
        username_label = tk.Label(credits_container, text="Username", bg="lawn green")
        username_label.grid(row=0, column=0)
        password_label = tk.Label(credits_container, text="Password", bg="lawn green")
        password_label.grid(row=1, column=0)
        self.username_entry = tk.Entry(credits_container, width=20, bg="green yellow", textvariable=self.username)
        self.username_entry.grid(row=0, column=1)
        self.password_entry = tk.Entry(credits_container, fg="red", width=20, bg="green yellow", show="*",
                                       textvariable=self.password).grid(row=1, column=1)
        empty_frame = tk.Label(credits_container, bg="lawn green").grid(row=2, columnspan=1, rowspan=1)
        forgot_password = tk.Button(credits_container, text="   Forgot passoword?  ", fg="red", bg="lawn green",
                                    borderwidth=0, command=lambda: self.do_forgot_password()).grid(row=3, columnspan=2)
        credits_container.pack()

        login_button = tk.Button(login_frame, text="Login", bg="lime green", command=lambda: self.do_login())
        login_button.place(relx=0.5, rely=0 / 3)
        back_button = tk.Button(login_frame, text="Back", bg="lime green",
                                command=lambda: self.controller.show_frame("StartPage")).place(relx=0.5, rely=1 / 3)

    def do_login(self):
        if self.valid():  # if username and password are correct
            self.controller.show_frame("StartPage")
            self.clear_entries()
        else:
            self.controller.show_frame("StartPage")
            self.clear_entries()

    def do_forgot_password(self):
        self.clear_entries()
        self.controller.show_frame("StartPage")


class SignUp(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is the sign up page.", font=controller.title_font)

        #label.pack(side="top", fill="x", padx=10, pady=10)
        label.grid(column=0, row=0, sticky="N")

        """Adding the labels required fields for the sign up page"""
        tk.Label(self,text="Name",font=controller.labels_font).grid(column=0, row=1, sticky=("N","W"))
        tk.Label(self, text="Last Name", font=controller.labels_font).grid(column=0, row=2, sticky=("N", "W"))
        tk.Label(self, text="Phone", font=controller.labels_font).grid(column=0, row=3, sticky=("N", "W"))
        tk.Label(self, text="Email", font=controller.labels_font).grid(column=0, row=4, sticky=("N", "W"))
        tk.Label(self, text="Password", font=controller.labels_font).grid(column=0, row=5, sticky=("N", "W"))
        tk.Label(self, text="Re-enter \n password", font=controller.labels_font).grid(column=0, row=6 , rowspan=2,
                                                                                      sticky=("N", "W"))

        """Creating entry fields and variables which will store data from the entry fields"""
        self.name = tk.StringVar()
        name_ent = tk.Entry(self, textvariable=self.name)
        name_ent.grid(column=0, row=1, sticky=("N","E"))

        self.last_name = tk.StringVar()
        last_name_ent = tk.Entry(self, textvariable=self.last_name)
        last_name_ent.grid(column=0, row=2, sticky=("N", "E"))

        self.phone = tk.StringVar()
        phone_ent = tk.Entry(self, textvariable=self.phone)
        phone_ent.grid(column=0, row=3, sticky=("N", "E"))

        self.email = tk.StringVar()
        email_ent = tk.Entry(self, textvariable=self.email)
        email_ent.grid(column=0, row=4, sticky=("N", "E"))

        self.password = tk.StringVar()
        password_ent = tk.Entry(self, show="*", textvariable=self.password)
        password_ent.grid(column=0, row=5, sticky=("N", "E"))

        self.password2 = tk.StringVar()
        password2_ent = tk.Entry(self, show="*", textvariable=self.password2)
        password2_ent.grid(column=0, row=7, sticky=("N", "E"))

        create_profile_btn = tk.Button(self,text="Create profile",command=self.click_create_profile)
        create_profile_btn.grid(column=1, row=8, sticky=("S","E"))

        self.test = tk.Label(self, text="Please complete your profile.")
        self.test.grid(column=0, row=9, sticky=("E","W"))

        back_btn = tk.Button(self, text="Back", command=lambda: controller.show_frame("StartPage"))
        back_btn.grid(column=0, row=8, sticky=("S","W"))

    def click_create_profile(self):
        name = self.name.get()
        surname = self.last_name.get()
        phone = self.phone.get()
        email  = self.email.get()
        password = self.password.get()
        password2 = self.password2.get()

        return_message = details_check(name, surname, email, phone, password, password2)
        self.test.configure(text=return_message)
        



if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
