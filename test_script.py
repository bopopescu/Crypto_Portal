import unittest
from extra_functions import details_check
from extra_functions import login_check
from main_file import *


# details_check(username, email, phone, pass1,pass2):

class MyTestCase(unittest.TestCase):

    #Testing if our detials function returns the correct message when all parameters are provided
    def test_details_function(self):
        self.assertEqual(details_check("hello","hello","hello","hello","hello"),
                        "Account created!")
    #tesing if the username filled is empty
    def test_details_function_username(self):
        self.assertEqual(details_check("","hello","hello","hello","hello"),
                        "Username Field is required!")

    # Testing details function when there are missing parameters
    def test_details_function_email(self):
        self.assertEqual(details_check("hello", "", "hello", "hello", "hello"),
                         "Email Filed is required!")

    #Tesing the phone field entry
    def test_details_function_phone(self):
        self.assertEqual(details_check("hello", "hello", "", "hello", "hello"),
                         "Phone Field is required!")

    #Tesing  the password function, for both passwords
    def test_details_function_pass1(self):
        self.assertEqual(details_check("hello", "hello", "hello", "", "hello"),
                         "Password field is required!")

    def test_details_function_pass2(self):
        self.assertEqual(details_check("hello", "hello", "hello", "hello", ""),
                         "Confirm Password field is required!")
    #checking for password mis match
    def test_details_function_pass1(self):
        self.assertEqual(details_check("hello", "hello", "hello", "gdfhdfb", "hello"),
                         "Password mismatch!")


     #Tesing in the login_check function return the required
    def test_login_check(self):
        self.assertEqual(login_check("username", "username"), "You have successfully logged in.")
        
    #Testing if the loging_check function returns correct message if fields are not complete     
    def test_login_check_(self):
        self.assertEqual(login_check("hello", ""), "Please fill in your details.")
        
    
if __name__ == '__main__':
    unittest.main()
