
import tkinter as tk

from api_functions import CoinsClass
coins_class = CoinsClass()
import tkinter.font as tk_fonts
import tkinter.ttk as ttk


class MarketCoin(tk.Frame):

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        b_g = "#e0ebeb"
        f_g = "gray31"
        families = ["Courier", "Comic Sans MS", "Arial Black", "Verdana", "Yu Gothic UI"]
        self.d_font = tk_fonts.Font(family=families[4], size=10, weight="bold")

        self.names = ["CURRENCY"]+[ val for val in coins_class.ret_name_list()[1:] ]
        self.ids = ["ID"]+[coins_class.ret_id(i) for i in self.names[1:]]
        self.symbol = ["SYMBOL"]

        self.price_usd = ["PRICE_USD"]
        self.percent_change_1h = ["PERCENT_CHANGE_1H"]
        self.percent_change_24h = ["PERCENT_CHANGE_24H"]
        self.percent_change_7d = ["PERCENT_CHANGE_7D"]

        self.number_of_rows = 7
        self.number_of_cols = 4

        # INSERTING VALUES IN VECTORS ( PRICE_USD, SYMBOLS, PERCENT_CHANGES )
        for i in range(1, self.number_of_rows):
            self.symbol.append(coins_class.re_symbol(self.ids[i]))
            self.price_usd.append(coins_class.re_market(self.ids[i]))

            self.percent_change_24h.append(coins_class.re_pc24h(self.ids[i]))
            self.percent_change_7d.append(coins_class.re_pc7d(self.ids[i]))
            self.percent_change_1h.append(coins_class.re_pc1h(self.ids[i]))

        # TABLE HEADERS CURRENCY, PRICE_USD, CHANGE_IH, CHANGE_24H, CHANGE_7D
        tk.Label(self, text="CURRENCY", fg=f_g, bg=b_g, font=self.d_font).grid(row=0, column=0, sticky="NEWS", columnspan=2, pady=5, padx=(10,5))
        tk.Label(self, text="PRICE\nUSD", fg=f_g, bg=b_g, font=self.d_font).grid(row=0, column=3, sticky="NEWS", columnspan=2, pady=5, padx=5)
        tk.Label(self, text="CHANGE\n1H", fg=f_g, bg=b_g, font=self.d_font).grid(row=0, column=6, sticky="NEWS", columnspan=2, pady=5, padx=5)
        tk.Label(self, text="CHANGE\n24H", fg=f_g, bg=b_g, font=self.d_font).grid(row=0, column=9, sticky="NEWS", columnspan=2, pady=5, padx=5)
        tk.Label(self, text="CHANGE\n7D", fg=f_g, bg=b_g, font=self.d_font).grid(row=0, column=12, sticky="NEWS", columnspan=2, pady=5, padx=5)

        self.rowconfigure(0, weight=1)

        for i in range(1, self.number_of_rows):
            r = i*2

            self.rowconfigure(r, weight=1)
            currency_frame = tk.Frame(self, bg=b_g)
            currency_frame.grid(row=r, column=0, columnspan=2, sticky="NEWS", pady=3, padx=(10, 0))

            tk.Label(currency_frame, text=self.names[i], fg=f_g, bg=b_g, font=self.d_font).grid(row=0, column=0, sticky="NEWS")
            tk.Label(currency_frame, text="( "+self.symbol[i]+" )", fg=f_g, bg=b_g, font=self.d_font).grid(row=1, column=1, sticky="W")

            p = self.price_usd[i]
            h_1 = self.percent_change_1h[i]
            h_24 = self.percent_change_24h[i]
            d_7 = self.percent_change_7d[i]

            price = tk.Label(self, text=p, fg=f_g, bg=b_g, font=self.d_font)
            price.grid(row=r, column=3, sticky="NEWS", columnspan=2, pady=5, padx=0)

            change_1_h = tk.Label(self, text=h_1+" %", fg=self.c_c(h_1), bg=b_g, font=self.d_font)
            change_1_h.grid(row=r, column=6, sticky="NEWS", columnspan=2, pady=3, padx=0)

            change_24_h = tk.Label(self, text=h_24+" %", fg=self.c_c(h_24), bg=b_g, font=self.d_font)
            change_24_h.grid(row=r, column=9, sticky="NEWS", columnspan=2, pady=3, padx=0)

            change_7_d = tk.Label(self, text=d_7+" %", fg=self.c_c(d_7), bg=b_g, font=self.d_font)
            change_7_d.grid(row=r, column=12, sticky="NEWS", columnspan=2, pady=3, padx=0)

            ttk.Separator(self, orient=tk.HORIZONTAL).grid(column=0, row=r-1, columnspan=15, sticky='we')

        # CONFIGURING COLUMNS
        for i in range(0, 13, 3):
            self.columnconfigure(i, weight=1)

        # INSERTING LINES INTO TABLE
        for i in range(2, 12, 3):
            ttk.Separator(self, orient=tk.VERTICAL).grid(column=i, row=0, rowspan=self.number_of_rows*2-1, sticky='ns')

        # REFRESH BUTTON
        # refresh_button = tk.Button(self, text="Refresh Feeds", font=self.d_font, fg=f_g, bg=b_g)
        #
        # refresh_button.grid(row=self.number_of_rows*2+1, column=0, columnspan=15, sticky="NEWS", pady=20)

    # RETURNS COLOR - RETURNS RED IF VALUE IS NEGATIVE ELSE BLUE
    def c_c(self, value):
        if value[0] == '-':
            return "orangered2"

        return "blue"

