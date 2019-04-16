
import tkinter as tk

# A page to allow changing of profile details, it will be reached via the profile settings button in the main page.
class Profile(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        #Fix the font to show the page properly
        label_ = tk.Label(self, text="Profile Settings")
        label_.grid(sticky="W")

        #database.get_username()
        tk.Label(self, text="Username").grid(column="2", columnspan="3", row="1")

        #get user info from database(emai;, phone and coin data)
        tk.Label(self, text="Email").grid(column="0", columnspan="3", row="3")
        tk.Label(self, text="Phone").grid(column="0", columnspan="3", row="5")


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

        #creating a function to post the changes to the database and take us back to the main page
        #Apply_changes = tk.Button(self, text="Page Two",command=)