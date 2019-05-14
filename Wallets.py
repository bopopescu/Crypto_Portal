import tkinter as tk
from api_functions import CoinsClass
from api_functions import TradesClass

# The page where our wallets will be created
coin_class = CoinsClass()
trades_class = TradesClass()


class Wallets(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.options_frame = tk.Frame(self)
        self.options_frame.grid(column="0", columnspan="2", row="0")

        main_page = tk.Button(self.options_frame, text="Main Page", command=lambda: controller.show_frame("MainPage"))
        main_page.grid(column="0", columnspan="2", row="0")

        log_out = tk.Button(self.options_frame, text="Logout", command=lambda: self.controller.show_frame("StartPage"))
        log_out.grid(column="3", row="0")
        """
            Creating a coins frame which will include a dropdown with coin options the user want to create a wallet for.
        """

        self.coin_frame = tk.LabelFrame(self, text=" Create a wallet", width=350, height=200)
        self.coin_frame.grid(column="0", columnspan="2", row="1", sticky="EW", padx=5, pady=5)
        tkvar = tk.StringVar(self)
        coin_choices = coin_class.ret_name_list()
        tkvar.set(coin_choices[0])
        self.add_coin_dropdown = tk.OptionMenu(self.coin_frame, tkvar, *coin_choices)
        self.add_coin_dropdown.grid(column="0", columnspan="4", row="1", padx=5, pady=5, sticky="EW")

        """
            Creating a entry with label for the amount of coin you have of the selected coin
        """

        tk.Label(self.coin_frame, text="Amount :").grid(column="0", columnspan="2", row="2", padx=5, pady=5, sticky="EW")
        self.amount_var = tk.StringVar(self)
        self.amount_entry = tk.Entry(self.coin_frame, textvariable=self.amount_var)
        self.amount_entry.grid(column="2", columnspan="2", row="2", padx=5, pady=5, sticky="EW")

        """
            The needs to be database function for storing the type of coin and value posted by the user, if must 
            also check that the user does not have an existing wallet for the selected coin.  
        """

        """
          Creating a button which allow the user to create a new wallet
          A user cannot have more than two wallets for one coin
        """
        def wallet_onclick():
            pass

        self.create_wallet_btn = tk.Button(self.coin_frame, text="Create Wallet")
        self.create_wallet_btn.grid(column="2", columnspan="2", row="3", padx=5, pady=5, sticky="EW")

        """
            Creating a frame to display the wallets information. 
        """
        self.view_wallet_frame = tk.LabelFrame(self, text=" Manage Wallets", width=350, height=200)
        self.view_wallet_frame.grid(column="0", columnspan="14", row="2", sticky="EW", padx=5, pady=5)

        """
            Creating a dropdown to list the wallets, the has to be a database function returning a list with coin type
            and value. 
        """
        tk_var = tk.StringVar(self)
        wallet_choices = coin_class.ret_name_list()
        tk_var.set(wallet_choices[0])
        self.view_coin_dropdown = tk.OptionMenu(self.view_wallet_frame, tk_var, *wallet_choices)
        self.view_coin_dropdown.grid(column="0", columnspan="2", row="0", padx=5, pady=5, sticky="EW")

        """
            Creating a frame to display basic information about the select wallet.
            Adding label markers to the frame that include Name,Market Value, Wallet value and timestamp
        """
        self.info_frame = tk.LabelFrame(self.view_wallet_frame, text=" Basic Information", width=350, height=200)
        self.info_frame.grid(column="0", columnspan="4", row="2", sticky="EW", padx=5, pady=5)

        tk.Label(self.info_frame, text="Name :").grid(row=0, column=0, columnspan="2",sticky="EW", padx=5, pady=5)
        tk.Label(self.info_frame, text="Rank :").grid(row=1, column=0, columnspan="2", sticky="EW", padx=5, pady=5)
        tk.Label(self.info_frame, text="Wallet Value :").grid(row=2, column=0, columnspan="2", sticky="EW", padx=5, pady=5)
        tk.Label(self.info_frame, text="Market Value in USD:").grid(row=3, column=0, columnspan="2", sticky="EW", padx=5, pady=5)


        """
            Named labels to hold the information of the basic info frame
        """
        self.name_info = tk.Label(self.info_frame, text="")
        self.name_info.grid(row=0, column=2, columnspan="2",sticky="EW", padx=5, pady=5)
        self.rank_info = tk.Label(self.info_frame, text="")
        self.rank_info.grid(row=1, column=2, columnspan="2",sticky="EW", padx=5, pady=5)
        self.wallet_value_info = tk.Label(self.info_frame, text="")
        self.wallet_value_info.grid(row=2, column=2, columnspan="2",sticky="EW", padx=5, pady=5)
        self.market_value_info = tk.Label(self.info_frame, text="")
        self.market_value_info.grid(row=3, column=2, columnspan="2",sticky="EW", padx=5, pady=5)
        self.time_info = tk.Label(self.info_frame, text="")
        self.time_info.grid(row=4, column=1, columnspan="4", sticky="EW", padx=5, pady=5)
        def view_Onclick():
            _id = coin_class.ret_id(wallet_choices[wallet_choices.index(tk_var.get())])
            self.name_info["text"] = coin_class.re_name(_id)
            self.rank_info["text"] = coin_class.ret_rank(_id)
            self.wallet_value_info["text"] = "database related"
            self.market_value_info["text"] = coin_class.re_market(_id)
            self.time_info["text"] = coin_class.re_timestamp(_id)

        """
            Onclick() of this button we supposed to display info related to the selected coin.
        """
        self.view_wallet_btn = tk.Button(self.view_wallet_frame, text="View", command=view_Onclick)
        self.view_wallet_btn.grid(column="2", columnspan="2", row="0", padx=5, pady=5, sticky="EW")
        """
            Onclick() of this button we supposed to remove the wallet related to the selected coin.
        """
        self.remove_wallet_btn = tk.Button(self.view_wallet_frame, text="Remove")
        self.remove_wallet_btn.grid(column="4", columnspan="2", row="0", padx=5, pady=5, sticky="EW")


        """
            Creating a frame to display trades related to the selected wallet
        """

        self.trades_frame = tk.LabelFrame(self.view_wallet_frame, text=" Trades", width=350, height=200)
        self.trades_frame.grid(column="5", columnspan="6", row="2", sticky="EW", padx=5, pady=5)

        tk_var_trades = tk.StringVar(self)
        trade_choices = trades_class.ret_name_list()
        tk_var_trades.set(trade_choices[0])
        self.view_trades_dropdown = tk.OptionMenu(self.trades_frame, tk_var_trades, *trade_choices)
        self.view_trades_dropdown.grid(column="0", columnspan="2", row="0", padx=5, pady=5, sticky="EW")

        tk.Label(self.trades_frame, text="Name :").grid(row=2, column=0, columnspan="2", sticky="EW", padx=5, pady=5)
        tk.Label(self.trades_frame, text="Price :").grid(row=3, column=0, columnspan="2", sticky="EW", padx=5, pady=5)
        tk.Label(self.trades_frame, text="Size :").grid(row=4, column=0, columnspan="2", sticky="EW", padx=5, pady=5)
        tk.Label(self.trades_frame, text="Transcation :").grid(row=5, column=0, columnspan="2", sticky="EW", padx=5, pady=5)

        self.trades_name = tk.Label(self.trades_frame, text="")
        self.trades_name.grid(row=2, column=2, columnspan="2", sticky="EW", padx=5, pady=5)

        self.trades_price = tk.Label(self.trades_frame, text="")
        self.trades_price.grid(row=3, column=2, columnspan="2", sticky="EW", padx=5, pady=5)

        self.trades_size = tk.Label(self.trades_frame, text="")
        self.trades_size.grid(row=4, column=2, columnspan="2", sticky="EW", padx=5, pady=5)

        self.trades_trans = tk.Label(self.trades_frame, text="")
        self.trades_trans.grid(row=5, column=2, columnspan="2", sticky="EW", padx=5, pady=5)

        def trades_Onclick():
            pos = trades_class.names_.index(tk_var_trades.get())
            self.trades_name["text"] = trades_class.ret_name(pos)
            self.trades_price["text"] = trades_class.ret_price(pos)
            self.trades_size["text"] = trades_class.ret_size(pos)
            self.trades_trans["text"] = trades_class.ret_transactions(pos)


        self.trades_btn = tk.Button(self.trades_frame, text="View trade", command=trades_Onclick)
        self.trades_btn.grid(column="2", columnspan="2", row="0", padx=5, pady=5, sticky="EW")