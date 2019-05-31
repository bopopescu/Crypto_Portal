from tkinter import *
import json
import hashlib
import os
import re
import database

mydatabase = database.Database()

def details_check(username, email, phone, pass1,pass2):

	return_message = ''
	if username == "":
		return "Username Field is required!"
	elif database.username_exist(username):
		return "Username exist"
	elif email == "":
		return "Email Filed is required!"
	elif phone == "":
		return "Phone Field is required!"
	elif pass1 == "":
		return "Password field is required!"
	elif pass2 == "":
		return "Confirm Password field is required!"
	elif pass1 != pass2:
		return "Password mismatch!"
	else:
		return "Account created!"

def login_check(username,password):
	return_message =''
	if username=="" or password=="":
		return_message="Please fill in your details."
		return return_message

	elif database.valid_login( username=username, password=password ):
		return_message = "You have successfully logged in."
		return return_message

	else:
		return "Incorrect login"


def wallet_check(username, amount, wallet_id):
	if wallet_id=="Select a coin":
		return "Please select a coin"

	elif mydatabase.wallet_exist(username=username, wallet_id=wallet_id) == True:
		return "Wallet already exist"

	elif amount == "":
		return "Amount not filled"
	else:
		return "Wallet created"
