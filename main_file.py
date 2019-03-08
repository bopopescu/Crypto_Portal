import tkinter as tk                # python 3
from tkinter import font  as tkfont # python 3
from extra_functions import pass_word_check


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
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is the sign-in page ", font=controller.title_font)
        label.grid(column=0, row=0, sticky="N")


        back = tk.Button(self, text="Back",
                           command=lambda: controller.show_frame("StartPage"))
        back.grid(column=0,row=1, sticky=("S","E"))


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

        return_message = pass_word_check(name, surname, email, phone, password, password2)
        self.test.configure(text=return_message)
        



if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
