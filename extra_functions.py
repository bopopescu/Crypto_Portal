from tkinter import *
import hashlib
import os
import re

def details_check(name, surname, email, phone, pass1,pass2):
	return_message = ''
	if name == "":
		return_message ="Name Field is required!"
	elif surname == "":
		return_message ="Name Field is required!"
	elif email == "":
		return_message ="Email Filed is required!"
	elif phone == "":
		return_message ="Phone Field is required!"
	elif pass1 == "":
		return_message = "Password field is required!"
	elif pass2 == "":
		return_message = "Confirm Password field is required!"
	elif pass1 != pass2:
		return_message = "Password mismatch!"
	else:
		return_message ="Account created!"

	return return_message
