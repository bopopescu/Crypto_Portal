
import tkinter as tk
import database
# A page to allow changing of profile details, it will be reached via the profile settings button in the main page.
class Profile(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        #Fix the font to show the page properly
        label_ = tk.Label(self, text="Profile Settings")
        label_.grid(row=0, column=1,sticky="W")

        #DISPLAY LABELS TO DISPLAY CURRENT USERS DETAILS
        tk.Label(self, text="Current details").grid(row=1, column=0,columnspan=2,sticky="EW")
        tk.Label(self, text="Username :").grid( row=2, column=0, sticky="E")
        tk.Label(self, text= "Email Address :").grid( row=3, column=0, sticky="E")
        tk.Label(self, text= "Cell Number :").grid( row=4, column=0, sticky="E")

        #CHANGE DETAILS TEXT LABELS
        tk.Label(self, text= "Change details").grid( row=1, column=2    , columnspan=2, sticky="WE")
        tk.Label(self, text= "Change password").grid( row=2, column=2, sticky="E")
        tk.Label(self, text= "Change Email address").grid( row=3, column=2, sticky="E")
        tk.Label(self, text= "Change Cell Number").grid( row=4, column=2, sticky="E")

        #BUTTONS
        tk.Button(self, text="change", command=lambda :self.change() ).grid(row=5, column=3)
        #tk.Button(self, text="change").grid(row=3, column=4)
        #tk.Button(self, text="change").grid(row=4, column=4)

        self.username_display = tk.Label(self, text="this is default")
        self.username_display.grid( row=2, column=1 )

        self.email_add_display = tk.Label(self, text="" )
        self.email_add_display.grid( row=3, column=1 )

        self.cell_num_display = tk.Label(self, text="" )
        self.cell_num_display.grid( row=4, column=1 )


        #entry_column=100

        self.new_password = tk.StringVar()
        new_password_entry = tk.Entry(self, textvariable=self.new_password )
        new_password_entry.grid(row=2, column=3)

        self.new_email = tk.StringVar()
        new_email = tk.Entry(self, textvariable=self.new_email)
        new_email.grid(column=3, row="3")

        self.new_phone = tk.StringVar()
        new_phone = tk.Entry(self, textvariable=self.new_phone)
        new_phone.grid(column=3, row="4")

        back_btn = tk.Button(self, text="Back", command=lambda: controller.show_frame("MainPage"))
        back_btn.grid(column=0, row=0, sticky="W")

    def change(self):
        print( "this is the change method" )
        if self.new_password != "":
            database.change_password(username=database.get_current_username(), new_password=self.new_password.get() )

        if self.new_email != "":
            database.change_email_add( username=database.get_current_username(), new_email_add=self.new_email.get() )

        if self.new_phone != "":
            database.change_cell_num( username=database.get_current_username(), new_cell_num=self.new_phone.get() )

    def update(self ):
        username = database.get_current_username()
        self.username_display["text"] = username
        self.email_add_display["text"] = database.get_email_add( username )
        self.cell_num_display["text"] = database.get_cell_num( username )