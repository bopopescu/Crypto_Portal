import unittest
import pyrebase
from extra_functions import details_check
from extra_functions import login_check
from main_file import *
# details_check(username, email, phone, pass1,pass2):

use_trades = TradesClass()

class MyTestCase(unittest.TestCase):
    """
        Testing the functions and classes created in the api_functions script
    """
    #Test that the function return a list for the dropdown menus
    def test_names_list(self):
        self.assertTrue(isinstance(TradesClass(), type(use_trades)))

    #Check if ret_name_list returns a list.
    def test_ret_name_list(self):
        self.assertTrue(isinstance(list(), type(use_trades.ret_name_list())))

    #Check if the function return a string type
    def test_ret_name(self):
        self.assertTrue(isinstance(str(), type(use_trades.ret_name(0))))

    #check if the function returns the correct unix time stamp
    def test_ret_time(self):
        self.assertTrue(isinstance(str(), type(use_trades.ret_time(0))))

    #Test that the price object is not a string
    def test_ret_price(self):
        self.assertFalse(isinstance(str(), type(use_trades.ret_price(0))))

    #check if the size is returned as a float object
    def test_ret_size(self):
        self.assertTrue(isinstance(float(), type(use_trades.ret_size(0))))

    """
        Tesing the functuions created in the extra functions.
    """
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
    def test_details_function_pass_mismatch(self):
        self.assertEqual(details_check("hello", "hello", "hello", "gdfhdfb", "hello"),
                         "Password mismatch!")


     #Tesing in the login_check function return the required
    def test_login_check_complete(self):
        self.assertEqual(login_check("username", "username"), "You have successfully logged in.")
        
    #Testing if the loging_check function returns correct message if fields are not complete     
    def test_login_check_incomplete(self):
        self.assertEqual(login_check("hello", ""), "Please fill in your details.")
        
    
if __name__ == '__main__':
    unittest.main()
