
import tkinter as tk
import database
# A page to allow changing of profile details, it will be reached via the profile settings button in the main page.
class Profile(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        #Fix the font to show the page properly
        label_ = tk.Label(self, text="Profile Settings")
        label_.grid(sticky="W")

        #DISPLAY LABELS
        tk.Label(self, text="Username :").grid( row=2, column=0)
        tk.Label(self, text= "Email Address :").grid( row=3, column=0)
        tk.Label(self, text= "Cell # :").grid( row=4, column=0)

        #tk.Label(self, text=database.get_current_username() ).grid(row=2, column=1)
        self.username_display = tk.Label(self, text="this is default")
        self.username_display.grid( row=2, column=1 )
        self.email_add_display = tk.Label(self, text="" )
        self.email_add_display.grid( row=3, column=1 )
        self.cell_num_display = tk.Label(self, text="" )
        self.cell_num_display.grid( row=4, column=1 )
        
        #Text entry to take in changes to the above details
        #We create functions to post the data to the database
        new_email_ = tk.StringVar()
        new_email = tk.Entry(self, textvariable=new_email_)
        new_email.grid(column="3", columnspan="3", row="3")

        new_phone_ = tk.StringVar()
        new_phone = tk.Entry(self, textvariable=new_phone_)
        new_phone.grid(column="3", columnspan="3", row="5")

        back_btn = tk.Button(self, text="Back", command=lambda: controller.show_frame("MainPage"))
        back_btn.grid(column="3", columnspan="3", row="7")

    def update_username_display(self ):
        username = database.get_current_username()
        self.username_display["text"] = username
        self.email_add_display["text"] = database.get_email_add( username )
        self.cell_num_display["text"] = database.get_cell_num( username )
