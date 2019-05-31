import tkinter as tk
from cryptography.fernet import Fernet
import tkinter.font as tk_fonts

# The page where our wallets portfolios will be created

class Encryption(tk.Frame):

    def __init__(self, parent, controller):
        b_g = "#d1e0e0"
        # b_g = "white"
        f_g = "gray31"
        families = ["Courier", "Comic Sans MS", "Arial Black", "Verdana", "Yu Gothic UI"]
        font = tk_fonts.Font(family=families[4], size=10, weight="bold")

        tk.Frame.__init__(self, parent, bg=b_g)
        self.controller = controller

        self.columnconfigure(0, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(5, weight=1)

        self.options_frame = tk.Frame(self, bg=b_g)
        self.options_frame.grid(column="0", columnspan="2", row="0")

        main_page = tk.Button(self.options_frame, text="Main Page", command=lambda: controller.show_frame("MainPage"), bg=b_g, fg=f_g, font=font)
        main_page.grid(column="0", columnspan="2", row="0", padx=10, pady=(30, 0))

        log_out = tk.Button(self.options_frame, text="Logout", bg=b_g, fg=f_g, font=font, command=lambda: self.controller.show_frame("StartPage"))
        log_out.grid(column="3", columnspan="2", row="0", padx=10, pady=(30, 0))

        # Encryption frame
        self.encryption_frame = tk.LabelFrame(self, text=" Encryption", bg=b_g, fg=f_g, font=font, width=350, height=200)
        self.encryption_frame.grid(row=2, column=0, columnspan=15, sticky="EW", padx=(50,50), pady=5, ipady=20)
        self.encryption_frame.columnconfigure(0, weight=1)
        self.encryption_frame.columnconfigure(2, weight=4)

        tk.Label(self.encryption_frame, text="Token", bg=b_g, fg=f_g, font=font, anchor="e").grid(row=2, column=0, columnspan=2, sticky="EW", padx=5, pady=5)
        self.token_variable = tk.StringVar()
        self.token_entry = tk.Entry(self.encryption_frame, textvariable=self.token_variable, bg=b_g, fg=f_g, font=font)
        self.token_entry.grid(row=2, column=2, columnspan=10, sticky="EW", padx=5, pady=(20, 5), ipadx=100, ipady=10)

        # Label for the encrypted token
        tk.Label(self.encryption_frame, text="Encrypted Token", bg=b_g, fg=f_g, font=font, anchor=tk.E).grid(row=5, column=0, columnspan=2, sticky="EW", padx=5, pady=5)
        self.token_string = tk.StringVar()
        self.token_label = tk.Entry(self.encryption_frame, bg=b_g, fg=f_g, font=font, textvariable=self.token_string, bd=0)
        self.token_label.grid(row=5, column=2, columnspan=2, sticky="EW", padx=5, pady=5, ipady=10)
        self.token_label.config(state="readonly")
        self.token_label.config(readonlybackground=b_g)

        # Label for the key
        tk.Label(self.encryption_frame, text="Encryption Key", bg=b_g, fg=f_g, font=font, anchor="e").grid(row=4, column=0, columnspan=2, sticky="EW", padx=5, pady=5)
        self.key_string = tk.StringVar()
        self.key_label = tk.Entry(self.encryption_frame, textvariable=self.key_string, bg=b_g, fg=f_g, font=font, bd=0)
        self.key_label.grid(row=4, column=2, columnspan=2, sticky="EW", padx=5, pady=5, ipady=10)
        self.key_label.config(state="readonly")
        self.key_label.config(readonlybackground=b_g)

        # Function to address reaction to the encryption btn
        def call_encrypt():

            key = Fernet.generate_key()
            cipher_suite = Fernet(key)
            if self.token_variable.get() != "":
                test = bytes(self.token_variable.get(), 'utf-8')
                cipher_text = cipher_suite.encrypt(test)

                self.token_label.config(state=tk.NORMAL)
                self.key_label.config(state=tk.NORMAL)

                self.key_label.delete('0', 'end')
                self.key_label.insert('0', key)

                self.token_label.delete('0', 'end')
                self.token_label.insert('0', cipher_text)

                self.token_label.config(state="readonly")
                self.key_label.config(state="readonly")

        self.btn_encryption = tk.Button(self.encryption_frame, bg=b_g, fg=f_g, font=font, text="Encrypt", command=call_encrypt)
        self.btn_encryption.grid(row=3, column=1, columnspan=4, padx=5, pady=5)

        # Decryption frame
        self.decryption_frame = tk.LabelFrame(self, text=" Decryption", bg=b_g, fg=f_g, font=font, width=350, height=200)
        self.decryption_frame.grid(row=3, column=0, columnspan=15, sticky="EW", padx=50, pady=5, ipady=20)

        self.decryption_frame.columnconfigure(0, weight=1)
        self.decryption_frame.columnconfigure(2, weight=4)

        tk.Label(self.decryption_frame, text="Encrypted Token", bg=b_g, fg=f_g, font=font, anchor="e").grid(row=0, column=0, columnspan=2, sticky="EW", padx=5, pady=5)
        self.encrypted_token_variable = tk.StringVar()
        self.encrypted_token_entry = tk.Entry(self.decryption_frame, textvariable=self.encrypted_token_variable, bg=b_g, fg=f_g, font=font)
        self.encrypted_token_entry.grid(row=0, column=2, columnspan=2, sticky="EW", padx=5, pady=(20, 5), ipadx=100, ipady=7)

        tk.Label(self.decryption_frame, text="Key", anchor="e", bg=b_g, fg=f_g, font=font).grid(row=1, column=0, columnspan=2, sticky="EW", padx=50, pady=5)
        self.key_variable = tk.StringVar()
        self.encrypted_key_entry = tk.Entry(self.decryption_frame, textvariable=self.key_variable, bg=b_g, fg=f_g, font=font)
        self.encrypted_key_entry.grid(row=1, column=2, columnspan=2, sticky="EW", padx=5, pady=5, ipadx=100, ipady=7)

        self.token_string = tk.StringVar()
        self.view_token = tk.Entry(self.decryption_frame, textvariable=self.token_label, bg=b_g, fg=f_g, font=font, bd=0)
        self.view_token.grid(row=4, column=2, columnspan=2, ipadx=100, ipady=7, sticky="WE", padx=5)
        self.view_token.config(state="readonly")
        self.view_token.config(readonlybackground=b_g)

        def call_decrypt():
            if self.key_variable.get() != "" and self.encrypted_token_variable.get() != "":
                test = bytes(self.key_variable.get(), 'utf-8')
                f = Fernet(bytes(test))
                string_need = bytes(str(self.encrypted_token_variable.get()), 'utf-8')
                #test2 = bytes(.encode(), 'utf-8')
                print(test)
                print(string_need)
                decrypted = f.decrypt(string_need)
                self.view_token["text"] = decrypted.decode("utf-8")
                self.view_token.config(state=tk.NORMAL)
                self.view_token.delete('0', 'end')
                self.view_token.insert('0', decrypted)
                self.view_token.config(state=tk.DISABLED)

        self.btn_encryption = tk.Button(self.decryption_frame, text="Decrypt", command=call_decrypt, bg=b_g, fg=f_g, font=font)
        self.btn_encryption.grid(row=3, column=1, columnspan=4, padx=5, pady=5)

        tk.Label(self.decryption_frame, text="Decrypted token", anchor='e', bg=b_g, fg=f_g, font=font).grid(row=4, column=0, columnspan=2, padx=5, sticky='WE')

    def update_page(self):
        # print("updating encryption")
        self.clear_entries()

    def clear_entries(self):
        # print("encryption clear entries")

        self.view_token.config(state=tk.NORMAL)
        self.token_label.config(state=tk.NORMAL)
        self.key_label.config(state=tk.NORMAL)

        self.view_token.delete(0, tk.END)
        self.view_token.insert(0, "")

        self.token_label.delete(0, tk.END)
        self.token_label.insert(0, "")

        self.key_label.delete(0, tk.END)
        self.key_label.insert(0, "")

        self.token_entry.delete(0, tk.END)
        self.token_entry.insert(0, "")

        self.encrypted_token_entry.delete(0, tk.END)
        self.encrypted_token_entry.insert(0, "")

        self.encrypted_key_entry.delete(0, tk.END)
        self.encrypted_key_entry.insert(0, "")

        self.view_token.config(state="readonly")
        self.token_label.config(state="readonly")
        self.key_label.config(state="readonly")
