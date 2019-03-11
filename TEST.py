import unittest
from extra_functions import details_check
from main_file import *
app = SampleApp()

class MyTestCase(unittest.TestCase):
    def test_title(self):
        self.assertEqual("Crypto-Portal", app.title())

    #Testing if our detials function returns the correct message when all parameters are provided
    def test_details_function(self):
        self.assertEqual(details_check("hello","hello","hello","hello","hello","hello"),
                         "Account created!")

    #Testing details function when there are missing parameters
    def test_details_functio_(self):
        self.assertEqual(details_check("hello", "hello", "", "hello", "hello", "hello"),
                         "Email Filed is required!")



if __name__ == '__main__':
unittest.main()
