
import tkinter as tk
import tkinter.font as tkfont
import extra_functions as extra_functions


class EntryWithPlaceholder():
    def __init__(self, entry, placeholder="PLACEHOLDER"):
        self.entry = entry
        self.placeholder = placeholder
        # print("self.placeholder = ", self.placeholder)
        # self.placeholder_color = color
        # print("self.placeholder_color =", self.placeholder_color )
        self.default_fg_color = self.entry['fg']

        self.entry.bind("<FocusIn>", self.foc_in)
        self.entry.bind("<FocusOut>", self.foc_out)

        self.put_placeholder()

    def put_placeholder(self):
        self.entry.insert(0, self.placeholder)
        self.entry.config(fg="gray")

    def foc_in(self, *args):
        # print("foc_in")
        if self.entry['fg'] == "gray":
            self.entry.delete('0', 'end')
            self.entry['fg'] = self.default_fg_color

    def foc_out(self, *args):
        # print("foc_out")
        if not self.entry.get():
            self.put_placeholder()


class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Crypto-Portal")
        # self.state("zoomed")
        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        self.padding = ""

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, SignIn, SignUp, MainPage):
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

        self.default_font = font = tkfont.Font(family="Times", size=15)
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
        if  result == True:
            # login
            self.controller.show_frame("MainPage")
        else:
            self.messege.set( result )

    def do_forgot_password(self):
        print("do_forgot_password")
        self.controller.show_frame("MainPage")


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

        button_font = tkfont.Font(family="Times", size=13)

        button1 = tk.Button(self, text="Sign in", bg=self.default_bg, fg="green", font=button_font,
                            command=lambda: controller.show_frame("SignIn"))
        button1.grid(row=1, column=0, ipadx=30, ipady=8)
        self.rowconfigure(1, weight=1)

        button2 = tk.Button(self, text="Sign up", fg="green", bg=self.default_bg, font=button_font,
                            command=lambda: controller.show_frame("SignUp"))
        button2.grid(row=2, column=0, ipadx=30, ipady=10, sticky="N", pady=(0, 100))
        self.rowconfigure(2, weight=1)


class SignUp(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.default_font = font = tkfont.Font(family="Times", size=15)
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
            self.controller.show_frame("MainPage")
        else:
            self.test.configure(text=return_message)


# The page where our wallets portfolios will be created
class MainPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        log_out = tk.Button(self, text="Back To StartPage",command=lambda: self.controller.show_frame("StartPage")).grid(sticky="NEWS")
        self.config(bg="yellow green")


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
