
import unittest2
from main_file import Greeter

class MyTestCase(unittest2.TestCase):
    def test_default_greeting_set(self):
        greeter = Greeter()
        self.assertEqual(greeter.message, 'Hello world!')

if __name__ == '__main__':
    unittest2.main()
