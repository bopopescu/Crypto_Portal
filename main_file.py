import tkinter as tk
import api_functions
import webbrowser


# The page where our wallets portfolios will be created
class MainPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.options_frame = tk.Frame(self)
        self.options_frame.grid(column="0", columnspan="2", row="0")

        profile = tk.Button(self.options_frame, text="Profile Settings",
                            command=lambda: controller.show_frame("Profile"))
        profile.grid(column="0", columnspan="2", row="0")

        wallets = tk.Button(self.options_frame, text="Wallets",
                            command=lambda: controller.show_frame("Wallets"))
        wallets.grid(column="2", columnspan="2", row="0")

        encryption = tk.Button(self.options_frame, text="Encryption", command=lambda: controller.show_frame("Encryption"))
        encryption.grid(column="4", columnspan="2", row="0")

        log_out = tk.Button(self.options_frame, text="Logout", command=lambda: self.controller.show_frame("StartPage"))
        log_out.grid(column="6", row="0")

        # create a Frame for the Text and Scrollbar
        self.txt_frame = tk.LabelFrame(self, text=" Article Information", width=350, height=200)
        self.txt_frame.grid(column="0", columnspan="2", row="5")
        # ensure a consistent GUI size
        self.txt_frame.grid_propagate(False)
        # implement stretchability
        self.txt_frame.grid_rowconfigure(0, weight=1)
        self.txt_frame.grid_columnconfigure(0, weight=1)

        # create a Text widget
        self.txt = tk.Text(self.txt_frame, borderwidth=3, relief="sunken")
        self.txt.config(font=("consolas", 12), undo=True, wrap='word')
        self.txt.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)

        # create a Scrollbar and associate it with txt
        self.scrollb = tk.Scrollbar(self.txt_frame, command=self.txt.yview)
        self.scrollb.grid(row=0, column=1, sticky='nsew')
        self.txt['yscrollcommand'] = self.scrollb.set

        # creating a frame for the article name and description
        self.hline_frame = tk.Frame(self)
        self.hline_frame.grid(column=0, columnspan=2, row=2, padx=5, pady=5)
        self.hline_frame.rowconfigure(0, weight=1)
        self.hline_frame.columnconfigure(0, weight=1)

        tkvar = tk.StringVar(self)
        test_api = api_functions.ArticlesClass()
        choices = test_api.tittle_source()
        tkvar.set(choices[0])

        self.pop_up_menu = tk.OptionMenu(self.hline_frame, tkvar, *choices)
        tk.Label(self.hline_frame, text="Choose an article").grid(row=1, column=1)
        self.pop_up_menu.grid(row=2, column=1)
        d = test_api.url_source()

        def change_dropdown(*args):
            i = choices.index(tkvar.get())
            a = test_api.articles_source()
            b = test_api.description_source()
            c = test_api.author_source()

            self.txt.config()
            self.txt.delete(1.0, tk.END)
            self.txt.insert('1.0', 'Source: ' + a[i] + '\n\nTitle: ' + choices[i] + '\n\nAuthor: ' + c[
                i] + '\n\nDescription: ' + b[i])
            return i

        def open_web():
            webbrowser.open(d[choices.index(tkvar.get())])

        self.link_btn = tk.Button(self.hline_frame, text="Read Full article", command=open_web)
        self.link_btn.grid(row=4, column=0, columnspan=2)
        tkvar.trace('w', change_dropdown)
    
    def update(self):
        nothing = "nothing"
