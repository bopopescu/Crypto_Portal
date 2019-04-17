
import tkinter as tk
import extra_functions
#from main_file import EntryWithPlaceholder
import database



class SignIn(tk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent)
        # self.con.state("zoomed")
        self.columnconfigure(0, weight=1)

        #DECLARING DEFAULT COLOR AND FONT
        self.default_font = font = tk.font.Font(family="Times", size=15)
        self.default_bg = "yellow green"

        canvas = tk.Canvas(self, bg="yellow green", bd=0)
        canvas.create_text(650, 140, text="Crypto Portal", anchor=tk.CENTER, font="Times 70 bold", fill="green")
        canvas.create_text(650, 140, text="Crypto Portal", anchor=tk.CENTER, font="Times 71 bold", fill="lime green")
        canvas.grid(row=0, column=0, sticky="NEWS", columnspan=10, rowspan=10)

        tk.Label(self, bg=self.default_bg).grid(row=0, column=0)
        self.rowconfigure(0, weight=10)



        self.username = tk.StringVar(self)
        self.username_entry = tk.Entry(self, bg=self.default_bg, font=self.default_font, textvariable=self.username,
                                  fg="green")
        self.username_entry.grid(row=1, column=0, ipady=10, pady=2, ipadx=40)
        self.rowconfigure(1, weight=1)
        EntryWithPlaceholder(self.username_entry, placeholder="Username")

        self.password = tk.StringVar(self)
        self.password_entry = tk.Entry(self, bg=self.default_bg, font=self.default_font, show="*",
                                  textvariable=self.password, fg="green")
        self.password_entry.grid(row=2, column=0, ipady=10, pady=2, ipadx=40)
        self.rowconfigure(2, weight=1)
        EntryWithPlaceholder(self.password_entry, placeholder="Password")

        self.messege = tk.StringVar()
        self.error_messege = tk.Label(self, text="", fg="red",bg=self.default_bg , font=self.default_font ,textvariable=self.messege).grid(row=3, column=0)

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
            self.controller.show_frame("MainPage")
            database.set_current_username( self.username.get() )
            #self.clear_entries()
        else:
            self.messege.set( result )

    def do_forgot_password(self):
        print("do_forgot_password")
        self.controller.show_frame("MainPage")

    def put_placeholder(self, entry , placeholder):
        entry.delete(0, 'end')
        entry.insert(0, placeholder)
        entry.config(fg="gray")

    def update(self):
        self.put_placeholder( entry=self.username_entry, placeholder="Username" )
        self.put_placeholder( entry=self.password_entry, placeholder="Password" )
        self.messege.set("")



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
