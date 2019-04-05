
import tkinter as tk
import Database as database


#print( "valid_login =", database.valid_login( username="reuben", password="matlala" ))
#database.create_user(username="reuben", password="matlala", email="reuben.mahloele@gmail.com", phone="1234567890")

def print_signUp_details( username, email, phone, pass1,pass2 ):
	print("usename =", username)
	print("email =", email)
	print("phone =", phone)
	print("pass1 =", pass1)
	print("pass2 =", pass2)

def details_check(username, email, phone, pass1,pass2):

	return_message = ''
	if username == "":
		return "Name Field is required!"
	elif database.username_exist( username ):
		return "Username already exist"
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
		database.create_user(username, email, phone, pass1)
		return_message ="Account created!"
	return return_message

def login_check(username,password):
	return_messgae=''
	if username=="" or password=="":
		return_message="Please fill in your details."
		return return_message

	elif username!="" and password!="":
		if database.valid_login( username, password ):
			return True
		else:
			return "Invalid username or password"

	else:
		return_message='You have succefully logged in.'
		return return_message
