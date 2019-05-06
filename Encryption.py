import tkinter as tk
import urllib.request, json
import extra_functions
import base64
from cryptography.fernet import Fernet


# The page where our wallets portfolios will be created
class Encryption(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.options_frame = tk.Frame(self)
        self.options_frame.grid(column="0", columnspan="2", row="0")

        main_page = tk.Button(self.options_frame, text="Main Page", command=lambda: controller.show_frame("MainPage"))
        main_page.grid(column="0", columnspan="2", row="0")

        log_out = tk.Button(self.options_frame, text="Logout", command=lambda: self.controller.show_frame("StartPage"))
        log_out.grid(column="3", columnspan="2", row="0")

        #Encryption frame
        self.encryption_frame = tk.LabelFrame(self, text=" Encryption", width=350, height=200)
        self.encryption_frame.grid(row=2, column=0, columnspan=15, sticky="EW", padx=5, pady=5)

        tk.Label(self.encryption_frame, text="Token").grid(row=2, column=0, columnspan=2, sticky="EW", padx=5, pady=5)
        self.token_variable = tk.StringVar()
        self.token_entry = tk.Entry(self.encryption_frame, textvariable=self.token_variable)
        self.token_entry.grid(row=2, column=2, columnspan=2, sticky="EW", padx=5, pady=5)

        #Label for the encrypted token
        tk.Label(self.encryption_frame, text="Encrypted Token").grid(row=5, column=0, columnspan=2, sticky="EW", padx=5, pady=5)
        self.token_label = tk.Label(self.encryption_frame, text="Token label")
        self.token_label.grid(row=5, column=2, columnspan=2, sticky="EW", padx=5, pady=5)

        #Label for the key
        tk.Label(self.encryption_frame, text="Encryption Key").grid(row=4, column=0, columnspan=2, sticky="EW", padx=5, pady=5)
        self.key_label = tk.Label(self.encryption_frame, text="Key label")
        self.key_label.grid(row=4, column=2, columnspan=2, sticky="EW", padx=5, pady=5)

        #Function to address reaction to the encryption btn
        def call_encrypt():
            key = Fernet.generate_key()
            cipher_suite = Fernet(key)
            if self.token_variable.get() != "":
                test =bytes(self.token_variable.get(), 'utf-8')
                cipher_text = cipher_suite.encrypt(test)
                self.token_label["text"] = cipher_text
                self.key_label["text"] = key


        self.btn_encryption = tk.Button(self.encryption_frame, text="Encrypt", command=call_encrypt)
        self.btn_encryption.grid(row=3, column=1, columnspan=4, padx=5, pady=5)

        #Decryption frame
        self.decryption_frame = tk.LabelFrame(self, text=" Decryption", width=350, height=200)
        self.decryption_frame.grid(row=3, column=0, columnspan=15, sticky="EW", padx=5, pady=5)

        tk.Label(self.decryption_frame, text="Encrypted Token", ).grid(row=0, column=0, columnspan=2, sticky="EW", padx=5, pady=5)
        self.encrypted_token_variable = tk.StringVar()
        self.encrypted_token_entry = tk.Entry(self.decryption_frame, textvariable=self.encrypted_token_variable)
        self.encrypted_token_entry.grid(row=0, column=2, columnspan=2, sticky="EW", padx=5, pady=5)

        tk.Label(self.decryption_frame, text="Key", ).grid(row=1, column=0, columnspan=2, sticky="EW", padx=5, pady=5)
        self.key_variable = tk.StringVar()
        self.encrypted_token_entry = tk.Entry(self.decryption_frame, textvariable=self.key_variable)
        self.encrypted_token_entry.grid(row=1, column=2, columnspan=2, sticky="EW", padx=5, pady=5)

        self.view_token = tk.Label(self.decryption_frame, text="Decrypted token")
        self.view_token.grid(row=4, column=2, columnspan=2, padx=5, pady=5)
        def call_decrypt():
            if self.key_variable.get() != "" and self.encrypted_token_variable.get() != "":
                test = bytes(self.key_variable.get(), 'utf-8')
                f = Fernet(test)
                test2 = bytes(self.encrypted_token_variable.get().encode(), 'utf-8')
                decrypted = f.decrypt(test2)
                self.view_token["text"] = decrypted


        self.btn_encryption = tk.Button(self.decryption_frame, text="Decrypt", command=call_decrypt)
        self.btn_encryption.grid(row=3, column=1, columnspan=4, padx=5, pady=5)

        tk.Label(self.decryption_frame, text="Decrypted token").grid(row=4, column=0, columnspan=2, padx=5, pady=5)




