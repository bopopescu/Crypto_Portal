
import tkinter as tk
import database
import tkinter.font as tk_fonts
import ctypes


# A page to allow changing of profile details, it will be reached via the profile settings button in the main page.
class Profile(tk.Frame):

    def __init__(self, parent, controller):
        b_g = "#d1e0e0"
        f_g = "gray31"
        families = ["Courier", "Comic Sans MS", "Arial Black", "Verdana", "Yu Gothic UI"]
        d_font = tk_fonts.Font(family=families[4], size=10, weight="bold")

        tk.Frame.__init__(self, parent, bg=b_g)
        self.controller = controller

        # Fix the font to show the page properly
        label_ = tk.Label(self, text="Profile Settings", bg=b_g, fg=f_g, font=d_font)
        label_.grid(row=0, column=1,sticky="W")

        #DISPLAY LABELS TO DISPLAY CURRENT USERS DETAILS
        tk.Label(self, text="Current details", bg=b_g, fg=f_g, font=d_font).grid(row=1, column=0, columnspan=2, sticky="EW")
        tk.Label(self, text="Username :", bg=b_g, fg=f_g, font=d_font).grid(row=2, column=0, sticky="E")
        tk.Label(self, text= "Email Address :", bg=b_g, fg=f_g, font=d_font).grid(row=3, column=0, sticky="E")
        tk.Label(self, text= "Cell Number :", bg=b_g, fg=f_g, font=d_font).grid(row=4, column=0, sticky="E")

        # CHANGE DETAILS TEXT LABELS
        tk.Label(self, text= "Change details", bg=b_g, fg=f_g, font=d_font).grid(row=1, column=2, columnspan=2, sticky="WE")
        tk.Label(self, text= "Change password", bg=b_g, fg=f_g, font=d_font).grid(row=2, column=2, sticky="E")
        tk.Label(self, text= "Change Email address", bg=b_g, fg=f_g, font=d_font).grid(row=3, column=2, sticky="E")
        tk.Label(self, text= "Change Cell Number", bg=b_g, fg=f_g, font=d_font).grid(row=4, column=2, sticky="E")

        # BUTTONS
        tk.Button(self, text="change", command=lambda:self.change(), bg=b_g, fg=f_g, font=d_font).grid(row=5, column=3)
        # tk.Button(self, text="change").grid(row=3, column=4)
        # tk.Button(self, text="change").grid(row=4, column=4)

        self.username_display = tk.Label(self, text="this is default", bg=b_g, fg=f_g, font=d_font)
        self.username_display.grid( row=2, column=1 )

        self.email_add_display = tk.Label(self, text="", bg=b_g, fg=f_g, font=d_font)
        self.email_add_display.grid(row=3, column=1)

        self.cell_num_display = tk.Label(self, text="", bg=b_g, fg=f_g, font=d_font)
        self.cell_num_display.grid(row=4, column=1)

        self.new_password = tk.StringVar()
        new_password_entry = tk.Entry(self, textvariable=self.new_password, bg=b_g, fg=f_g, font=d_font)
        new_password_entry.grid(row=2, column=3)

        self.new_email = tk.StringVar()
        new_email = tk.Entry(self, textvariable=self.new_email, bg=b_g, fg=f_g, font=d_font)
        new_email.grid(column=3, row="3")

        self.new_phone = tk.StringVar()
        new_phone = tk.Entry(self, textvariable=self.new_phone, bg=b_g, fg=f_g, font=d_font)
        new_phone.grid(column=3, row="4")

        back_btn = tk.Button(self, text="Back", command=lambda: controller.show_frame("MainPage"), bg=b_g, fg=f_g, font=d_font)
        back_btn.grid(column=0, row=0, sticky="W")

    def change(self):
        # print("this is the change method")
        new_password = self.new_password.get()
        new_email = self.new_email.get()
        new_phone = self.new_phone.get()
        print(new_password, new_phone, new_email)
        if new_password != "":
            res = ctypes.windll.user32.MessageBoxW(0, "Are you sure you want to change password?", "Crypto Portal", 1)
            if res == 1:
                database.change_password(username=database.get_current_username(), new_password=new_password)

        if new_email != "":
            res = ctypes.windll.user32.MessageBoxW(0, "Are you sure you want to change email address?", "Crypto Portal", 1)
            if res == 1:
                database.change_email_add(username=database.get_current_username(), new_email_add=new_email)

        if new_phone != "":
            res = ctypes.windll.user32.MessageBoxW(0, "Are you sure you want to change cell?", "Crypto Portal", 1)
            if res == 1:
                database.change_cell_num( username=database.get_current_username(), new_cell_num=new_phone)

    def update_page(self):
        print("updating profile")

        username = self.controller.get_current_username()
        # print("current_username =", username)
        self.username_display["text"] = username

        user_email = database.get_email_add(username)
        # print("user_email =", user_email)
        self.email_add_display["text"] = user_email

        user_cell = database.get_cell_num(username)
        # print("user_cell =", user_cell)
        self.cell_num_display["text"] = user_cell
