import tkinter as tk
import urllib.request, json
import api_functions
import webbrowser
from api_functions import ArticlesClass
from api_functions import TradesClass
from api_functions import CoinsClass
from MarketHelper import MarketCoin
import tkinter.font as tk_fonts


article_class = ArticlesClass()
coins_class = CoinsClass()
trades_class = TradesClass()

# The page where our wallets portfolios will be created


class MainPage(tk.Frame):

    def __init__(self, parent, controller):
        b_g = "#d1e0e0"
        # b_g = "white"
        f_g = "gray31"
        families = ["Courier", "Comic Sans MS", "Arial Black", "Verdana", "Yu Gothic UI"]
        self.d_font = tk_fonts.Font(family=families[4], size=10, weight="bold")

        tk.Frame.__init__(self, parent, bg=b_g)
        self.controller = controller

        self.options_frame = tk.LabelFrame(self, text="Navigate to ", bg=b_g, font=self.d_font, fg=f_g)
        self.options_frame.grid(column=0, columnspan=2, rowspan=3, row=0, pady=(20, 5), sticky="NEWS", padx=20)

        # adding elements in navigation
        navigation = Navigation(parent=self.options_frame, controller=controller)
        navigation.grid(column=0, columnspan=2, row=0, pady=5, sticky="NEWS", padx=5)

        # create a Frame for the Text and Scrollbar
        self.txt_frame = NewsFrame(parent=self, controller=self.controller, text=" Article Information", width=350, height=150)
        self.txt_frame.grid(column="0", columnspan=3, row=6, rowspan=1, sticky="NEWS", pady=1, padx=20)
        # ensure a consistent GUI size
        self.txt_frame.grid_propagate(False)
        # implement stretchability
        self.txt_frame.grid_rowconfigure(0, weight=1)
        self.txt_frame.grid_columnconfigure(0, weight=1)

        tkvar = tk.StringVar(self)
        choices = article_class.tittle_source()
        tkvar.set(choices[0])

        # creating a frame for the article name and description
        self.hline_frame = HeadLine(parent=self, controller=self.controller, tkvar=tkvar, bg=b_g)
        self.hline_frame.grid_propagate(False)
        self.hline_frame.grid(column=0, columnspan=2, rowspan=2, row=3, padx=20, pady=10, sticky="NEWS")

        self.markets_trades_frame = tk.LabelFrame(self, text="Market Trades", bg=b_g, font=self.d_font, fg=f_g)
        self.markets_trades_frame.grid(row=0, column=2, sticky="NEWS", rowspan=6, padx=(10, 20), pady=20)
        self.markets_trades_frame.columnconfigure(0, weight=1)

        markets_frame = tk.Frame(self.markets_trades_frame, bg=b_g)
        markets_frame.grid(row=0, column=0, sticky="NEWS", padx=5, pady=5)
        markets_frame.columnconfigure(0, weight=1)
        markets_frame.rowconfigure(0, weight=1)
        self.markets = MarketCoin(markets_frame, bg="#e0ebeb")
        self.markets.grid(row=0, column=0, sticky="NEWS", pady=(10, 5), padx=10)

        self.columnconfigure(0, weight=3)
        self.columnconfigure(2, weight=5)

        def change_dropdown(*args):
            self.txt_frame.change_dropdown(tkvar)

        tkvar.trace('w', change_dropdown)

    def update_page(self):
        print("updating MainPage")
        nothing = "nothing"


class Navigation(tk.Frame):
    def __init__(self, parent, controller, *args, **kwargs):
        self.parent = parent
        self.controller = controller

        b_g = "#e0ebeb"
        f_g = "gray31"
        families = ["Courier", "Comic Sans MS", "Arial Black", "Verdana", "Yu Gothic UI"]
        self.d_font = tk_fonts.Font(family=families[4], size=10, weight="bold")

        tk.Frame.__init__(self, parent, *args, **kwargs, bg=b_g)

        profile = tk.Button(parent, text="Profile Settings", command=lambda: controller.show_frame("Profile"), fg=f_g, bg=b_g, font=self.d_font)
        profile.grid(column=0, columnspan=2, rowspan=2, row=0, sticky="NEWS", pady=5, padx=5)

        log_out = tk.Button(parent, text="Logout", command=lambda: self.controller.show_frame("StartPage"), fg=f_g, bg=b_g, font=self.d_font)
        log_out.grid(column=2, row=0, columnspan=2, rowspan=2, sticky="NEWS", pady=5, padx=5)

        show_encryption = tk.Button(parent, text="show_encryption",
                                    command=lambda: self.controller.show_frame("Encryption"), fg=f_g, bg=b_g, font=self.d_font)
        show_encryption.grid(row=2, column=0, rowspan=2, columnspan=2, sticky="NEWS", pady=5, padx=5)

        show_wallets = tk.Button(parent, text="show_wallets",
                                 command=lambda: self.controller.show_frame("Wallets"), fg=f_g, bg=b_g, font=self.d_font)
        show_wallets.grid(row=2, column=2, rowspan=2, columnspan=2, sticky="NEWS", pady=5, padx=5)

        for i in range(0, 4):
            parent.columnconfigure(i, weight=1)
            parent.rowconfigure(i, weight=1)


class NewsFrame(tk.LabelFrame):
    def __init__(self, parent, controller, *args, **kwargs):
        b_g = "#d1e0e0"
        f_g = "gray31"
        families = ["Courier", "Comic Sans MS", "Arial Black", "Verdana", "Yu Gothic UI"]
        self.d_font = tk_fonts.Font(family=families[4], size=10, weight="bold")

        tk.LabelFrame.__init__(self, parent, *args, **kwargs)
        self.config(bg=b_g)
        self.config(font=self.d_font)
        self.config(fg=f_g)

        self.parent = parent
        self.controller = controller
        # create a Text widget
        self.txt = tk.Text(self, borderwidth=3, relief="sunken", font=self.d_font, bg=b_g, fg=f_g)
        self.txt.config(font=("consolas", 12), undo=True, wrap='word')
        self.txt.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)

        # create a Scrollbar and associate it with txt
        self.scrollb = tk.Scrollbar(self, command=self.txt.yview)
        self.scrollb.grid(row=0, column=1, sticky='nsew')
        self.txt['yscrollcommand'] = self.scrollb.set

        self.choices = article_class.tittle_source()

    def change_dropdown(self, tkvar, *args):
        # print("change_dropdown")
        i = self.choices.index(tkvar.get())
        a = article_class.articles_source()
        b = article_class.description_source()
        c = article_class.author_source()

        self.txt.config(state=tk.NORMAL)
        self.txt.config()
        self.txt.delete(1.0, tk.END)
        self.txt.insert('1.0', 'Source: ' + a[i] + '\n\nTitle: ' + self.choices[i] + '\n\nAuthor: ' + c[i] + '\n\nDescription: ' + b[i])
        self.txt.config(state=tk.DISABLED)
        return i


class HeadLine(tk.Frame):
    def __init__(self, parent, controller, tkvar, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)

        # tkvar = tk.StringVar(self)
        choices = article_class.tittle_source()
        tkvar.set(choices[0])

        self.parent = parent
        self.controller = controller

        b_g = "#d1e0e0"
        f_g = "gray31"
        families = ["Courier", "Comic Sans MS", "Arial Black", "Verdana", "Yu Gothic UI"]
        self.d_font = tk_fonts.Font(family=families[4], size=10, weight="bold")

        for i in range(0, 2):
            self.columnconfigure(i, weight=1)

        self.pop_up_menu = tk.OptionMenu(self, tkvar, *choices)
        tk.Label(self, text="Choose an article", fg=f_g, font=self.d_font, bg=b_g).grid(row=1, column=0, columnspan=2, sticky="NEWS", pady=(10, 5))
        self.pop_up_menu.grid(row=2, column=0, columnspan=2, sticky="NEWS", pady=5)
        self.pop_up_menu.config(bg=b_g)
        self.pop_up_menu.config(fg=f_g)
        self.pop_up_menu.config(font=self.d_font)

        self.grid_propagate(False)

        d = article_class.url_source()

        def open_web():
            webbrowser.open(d[choices.index(tkvar.get())])

        def show_encryption():
            print("show encryption")
            self.controller.show_frame("Encryption")

        self.link_btn = tk.Button(self, text="Read Full article", command=open_web, font=self.d_font, fg=f_g, bg=b_g)
        self.link_btn.grid(row=3, column=0, columnspan=2, pady=5)
