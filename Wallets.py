import tkinter as tk
from api_functions import CoinsClass
from api_functions import TradesClass
import tkinter.font as tk_fonts
import database
import extra_functions
import ctypes
import matplotlib.pyplot as plt

# The page where our wallets will be created
coin_class = CoinsClass()
trades_class = TradesClass()
mydatabase = database.Database()

class Wallets(tk.Frame):

    def __init__(self, parent, controller):

        b_g = "#e0ebeb"
        f_g = "gray31"
        families = ["Courier", "Comic Sans MS", "Arial Black", "Verdana", "Yu Gothic UI"]
        d_font = tk_fonts.Font(family=families[4], size=10, weight="bold")

        tk.Frame.__init__(self, parent, bg=b_g)
        self.controller = controller

        self.options_frame = tk.Frame(self, bg="white")
        self.options_frame.grid(column=0, columnspan=2, row=0, pady=(10, 5))

        main_page = tk.Button(self.options_frame, text="Main Page", command=lambda: controller.show_frame("MainPage"), bg=b_g, fg=f_g, font=d_font)
        main_page.grid(column=0, row=0)

        log_out = tk.Button(self.options_frame, text="Logout", command=lambda: self.controller.show_frame("StartPage"), bg=b_g, fg=f_g, font=d_font)
        log_out.grid(column=1, row=0)

        # Creating a coins frame which will include a dropdown with coin options the user want to create a wallet for.
        self.coin_frame = CreateWallets(parent=self, controller=self.controller, text=" Create a wallet", width=350, height=200, bg=b_g, fg=f_g, font=d_font)
        self.coin_frame.grid(column=0, columnspan=10, row=1, sticky="NEWS", padx=20, pady=5)

        # Creating a frame to display the wallets information.
        self.view_wallet_frame = ManageWallets(parent=self, controller=self.controller, text=" Manage Wallets", width=350, height=300, bg=b_g, fg=f_g, font=d_font)
        self.view_wallet_frame.grid(column=0, columnspan=14, row=2, sticky="EW", padx=20, pady=5)

        # Creating a graphs frame to display the related graphs
        self.graphs_frame = DisplayGraphs(parent=self, controller=self.controller, text=" Graphs", width=350, height=300, bg=b_g, fg=f_g, font=d_font)
        self.graphs_frame.grid(column=0, columnspan=14, row=3, sticky="EW", padx=20, pady=5)

        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=4)
        self.columnconfigure(0, weight=1)

    def update_page(self):
        print("updating wallets")

class DisplayGraphs(tk.LabelFrame):
    def __init__(self, parent, controller, *args, **kwargs):
        tk.LabelFrame.__init__(self, parent, *args, **kwargs)
        self.propagate(False)
        self.controller = controller
        b_g = "#e0ebeb"
        f_g = "gray31"
        families = ["Courier", "Comic Sans MS", "Arial Black", "Verdana", "Yu Gothic UI"]
        d_font = tk_fonts.Font(family=families[4], size=10, weight="bold")
    
        def plot_pie_chart():
            labels = plot_data.ret_name_list()
            sizes = plot_data._vol24h_
            colors = ['gold', 'yellowgreen', 'red', 'lightcoral', 'lightskyblue']
            explode = (0.1, 0, 0, 0, 0)  # explode 1st slice

            # Plot
            plt.pie(sizes, explode=explode, labels=labels, colors=colors,
                    autopct='%1.1f%%', shadow=True, startangle=140)

            plt.axis('equal')
            plt.show()

        self.pie_chart = tk.Button(self, text="Pie Chart", bg=b_g, fg=f_g, font=d_font, command=plot_pie_chart)
        self.pie_chart.grid(column="1", columnspan="2", row="1", padx=5, pady=5, sticky="EW")
        
        
class ManageWallets(tk.LabelFrame):
    def __init__(self, parent, controller, *args, **kwargs):
        self.controller = controller
        b_g = "#e0ebeb"
        f_g = "gray31"
        families = ["Courier", "Comic Sans MS", "Arial Black", "Verdana", "Yu Gothic UI"]
        d_font = tk_fonts.Font(family=families[4], size=10, weight="bold")

        tk.LabelFrame.__init__(self, parent, *args, **kwargs)
        self.propagate(False)
        self.grid_propagate(False)

        # Creating a dropdown to list the wallets, the has to be a database function returning a list with coin type
        # and value
        tk_var = tk.StringVar(self)
        wallet_choices = coin_class.ret_name_list()
        tk_var.set(wallet_choices[0])
        self.view_coin_dropdown = tk.OptionMenu(self, tk_var, *wallet_choices)
        self.view_coin_dropdown.grid(column="0", columnspan="2", row="0", padx=5, pady=5, sticky="EW")
        self.view_coin_dropdown.config(bg=b_g)
        self.view_coin_dropdown.config(fg=f_g)
        self.view_coin_dropdown.config(font=d_font)
        # self.view_coin_dropdown.propagate(False)
        # self.view_coin_dropdown.grid_propagate(False)

        # Creating a frame to display basic information about the select wallet.
        # Adding label markers to the frame that include Name,Market Value, Wallet value and timestamp
        self.info_frame = tk.LabelFrame(self, text=" Basic Information", width=350, height=200, bg=b_g, fg=f_g, font=d_font)
        self.info_frame.grid(column=0, columnspan=4, row=2, sticky="EW", padx=5, pady=5)
        self.columnconfigure(0, weight=1)
        self.info_frame.propagate(False)
        self.info_frame.grid_propagate(False)

        l_n = LabelName(self.info_frame, self.controller, text="Name :")
        l_n.grid(row=0, column=0, columnspan="2", sticky="EW", padx=5, pady=5)

        l_r = LabelName(self.info_frame, self.controller, text="Rank :")
        l_r.grid(row=1, column=0, columnspan="2", sticky="EW", padx=5, pady=5)

        l_w = LabelName(self.info_frame, self.controller, text="Wallet Value :")
        l_w.grid(row=2, column=0, columnspan="2", sticky="EW", padx=5, pady=5)

        l_m = LabelName(self.info_frame, self.controller, text="Market Value in USD:")
        l_m.grid(row=3, column=0, columnspan="2", sticky="EW", padx=5, pady=5)

        # Named labels to hold the information of the basic info frame
        self.name_info = tk.Label(self.info_frame, text="", bg=b_g, fg=f_g, font=d_font)
        self.name_info.grid(row=0, column=2, columnspan=2, sticky="EW", padx=5, pady=5)

        self.rank_info = tk.Label(self.info_frame, text="", bg=b_g, fg=f_g, font=d_font)
        self.rank_info.grid(row=1, column=2, columnspan=2, sticky="NEWS", padx=5, pady=5)

        self.wallet_value_info = tk.Label(self.info_frame, text="", bg=b_g, fg=f_g, font=d_font)
        self.wallet_value_info.grid(row=2, column=2, columnspan=2, sticky="NEWS", padx=5, pady=5)

        self.market_value_info = tk.Label(self.info_frame, text="", bg=b_g, fg=f_g, font=d_font)
        self.market_value_info.grid(row=3, column=2, columnspan=2, sticky="NEWS", padx=5, pady=5)

        self.time_info = tk.Label(self.info_frame, text="", bg=b_g, fg=f_g, font=d_font)
        self.time_info.grid(row=4, column=1, columnspan=4, sticky="NEWS", padx=5, pady=5)

        def view_Onclick():
            _id = coin_class.ret_id(wallet_choices[wallet_choices.index(tk_var.get())])
            self.name_info["text"] = coin_class.re_name(_id)
            self.rank_info["text"] = coin_class.ret_rank(_id)
            self.wallet_value_info["text"] = mydatabase.get_amount(username=self.controller.get_current_username(), wallet_id=_id)
            self.market_value_info["text"] = coin_class.re_market(_id)
            self.time_info["text"] = coin_class.re_timestamp(_id)

        # FRAME CONTAINING OPTIONS
        self.wallets_options = tk.Frame(self)
        self.wallets_options.grid(row=0, column=2, columnspan=1)

        # Onclick() of this button we supposed to display info related to the selected coin.
        self.view_wallet_btn = tk.Button(self.wallets_options, text="View", command=view_Onclick, bg=b_g, fg=f_g, font=d_font)
        self.view_wallet_btn.grid(column=2, columnspan=1, row=0, padx=5, pady=5, sticky="NEWS")

        # Onclick() of this button we supposed to remove the wallet related to the selected coin.
        self.remove_wallet_btn = tk.Button(self.wallets_options, text="Remove", bg=b_g, fg=f_g, font=d_font)
        self.remove_wallet_btn.grid(column=4, columnspan=1, row=0, padx=5, pady=5, sticky="NEWS")

        # Creating a frame to display trades related to the selected wallet
        self.trades_frame = tk.LabelFrame(self, text=" Trades", width=350, height=200, bg=b_g, fg=f_g, font=d_font)
        self.trades_frame.grid(column=5, columnspan=6, row=2, sticky="NEWS", padx=5, pady=(5, 10))
        self.columnconfigure(5, weight=1)
        self.trades_frame.propagate(False)
        self.trades_frame.grid_propagate(False)

        tk_var_trades = tk.StringVar(self)
        trade_choices = trades_class.ret_name_list()
        tk_var_trades.set(trade_choices[0])
        self.view_trades_dropdown = tk.OptionMenu(self.trades_frame, tk_var_trades, *trade_choices)
        self.view_trades_dropdown.grid(column=0, columnspan=1, row=0, padx=5, pady=5, sticky="EW")
        self.view_trades_dropdown.config(bg=b_g)
        self.view_trades_dropdown.config(fg=f_g)
        self.view_trades_dropdown.config(font=d_font)

        label_name = LabelName(self.trades_frame, self.controller, text="Name :")
        label_name.grid(row=2, column=0, columnspan="2", sticky="EW", padx=5, pady=5)

        l_p = LabelName(self.trades_frame, controller=self.controller, text="Price :")
        l_p.grid(row=3, column=0, columnspan="2",  sticky="EW", padx=5, pady=5)

        l_s = LabelName(self.trades_frame, self.controller, text="Size :")
        l_s.grid(row=4, column=0, columnspan="2", sticky="EW", padx=5, pady=5)

        l_t = LabelName(self.trades_frame, self.controller, text="Transaction :")
        l_t.grid(row=5, column=0, columnspan="2", sticky="EW", padx=5, pady=5)

        self.trades_name = tk.Label(self.trades_frame, text="", bg=b_g, fg=f_g, font=d_font)
        self.trades_name.grid(row=2, column=2, columnspan="2", sticky="EW", padx=5, pady=5)

        self.trades_price = tk.Label(self.trades_frame, text="", bg=b_g, fg=f_g, font=d_font)
        self.trades_price.grid(row=3, column=2, columnspan="2", sticky="EW", padx=5, pady=5)

        self.trades_size = tk.Label(self.trades_frame, text="", bg=b_g, fg=f_g, font=d_font)
        self.trades_size.grid(row=4, column=2, columnspan="2", sticky="EW", padx=5, pady=5)

        self.trades_trans = tk.Label(self.trades_frame, text="", bg=b_g, fg=f_g, font=d_font)
        self.trades_trans.grid(row=5, column=2, columnspan="2", sticky="EW", padx=5, pady=5)

        def trades_Onclick():
            pos = trades_class.names_.index(tk_var_trades.get())
            self.trades_name["text"] = trades_class.ret_name(pos)
            self.trades_price["text"] = trades_class.ret_price(pos)
            self.trades_size["text"] = trades_class.ret_size(pos)
            self.trades_trans["text"] = trades_class.ret_transactions(pos)

        self.trades_btn = tk.Button(self.trades_frame, text="View trade", command=trades_Onclick, bg=b_g, fg=f_g,
                                    font=d_font)
        self.trades_btn.grid(column=2, columnspan=2, row=0, padx=5, pady=5, sticky="EW")

        # self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)

class CreateWallets(tk.LabelFrame):
    def __init__(self, parent, controller, *args, **kwargs):
        tk.LabelFrame.__init__(self, parent, *args, **kwargs)
        self.propagate(False)
        self.controller = controller
        b_g = "#e0ebeb"
        f_g = "gray31"
        families = ["Courier", "Comic Sans MS", "Arial Black", "Verdana", "Yu Gothic UI"]
        d_font = tk_fonts.Font(family=families[4], size=10, weight="bold")

        tkvar = tk.StringVar(self)
        coin_choices = coin_class.ret_name_list()
        tkvar.set(coin_choices[0])
        self.add_coin_dropdown = tk.OptionMenu(self, tkvar, *coin_choices)
        self.add_coin_dropdown.grid(column="0", columnspan="4", row="1", padx=5, pady=5, sticky="EW")
        self.add_coin_dropdown.config(bg=b_g)
        self.add_coin_dropdown.config(fg=f_g)
        self.add_coin_dropdown.config(font=d_font)

        # Creating a entry with label for the amount of coin you have of the selected coin
        tk.Label(self, text="Amount :", bg=b_g, fg=f_g, font=d_font).grid(column="0", columnspan="2",
                                                                                     row="2", padx=5, pady=5,
                                                                                     sticky="EW")
        self.amount_var = tk.StringVar(self)
        self.amount_entry = tk.Entry(self, textvariable=self.amount_var, bg=b_g, fg=f_g, font=d_font)
        self.amount_entry.grid(column="2", columnspan="2", row="2", padx=5, pady=5, sticky="NEWS")

        def wallet_onclick():
            print("wallet onclick")
            wallet_id = coin_class.ret_id(tkvar.get())
            username = self.controller.get_current_username()
            amount = self.amount_var.get()
            message = extra_functions.wallet_check(username=username, wallet_id=wallet_id, amount=amount)

            if message == "Wallet created":
                mydatabase.create_wallet(username=username, wallet_id=wallet_id, amount=amount)
            ctypes.windll.user32.MessageBoxW(0, message, "Crypto Portal", 1)

        self.create_wallet_btn = tk.Button(self, text="Create Wallet", bg=b_g, fg=f_g, font=d_font, command=wallet_onclick)
        self.create_wallet_btn.grid(column=2, columnspan=2, row=3, padx=5, pady=5, sticky="EW")

        self.error_message = tk.Label(self, text="", fg="red", font=d_font, bg=b_g)
        self.error_message.grid(row=4, column=2)

class LabelName(tk.Label):
    def __init__(self, parent, controller, *args, **kwargs):
        self.controller = controller
        tk.Label.__init__(self, parent, *args, **kwargs)

        b_g = "#e0ebeb"
        f_g = "gray31"
        families = ["Courier", "Comic Sans MS", "Arial Black", "Verdana", "Yu Gothic UI"]
        d_font = tk_fonts.Font(family=families[4], size=10, weight="bold")

        self.config(anchor="e")
        self.config(bg=b_g)
        self.config(fg=f_g)
        self.config(font=d_font)
