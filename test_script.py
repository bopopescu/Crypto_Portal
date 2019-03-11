import unittest
from extra_functions import details_check
from extra_functions import login_check
from main_file import *

class MyTestCase(unittest.TestCase):
    #Testing if our detials function returns the correct message when all parameters are provided
    def test_details_function(self):
        self.assertEqual(details_check("hello","hello","hello","hello","hello","hello"),
                         "Account created!")

    #Testing details function when there are missing parameters
    def test_details_functio_(self):
        self.assertEqual(details_check("hello", "hello", "", "hello", "hello", "hello"),
                         "Email Filed is required!")

     #Tesing in the login_check function return the required   
    def test_login_check(self):
        self.assertEqual(login_check("hello","world"),"Please fill in your details.")
        
    #Testing if the loging_check function returns correct message if fields are not complete     

    def test_login_check_(self):
        self.assertEqual(login_check("hello","world"),"You have succefully logged in.")
        
    
if __name__ == '__main__':
    unittest.main()
