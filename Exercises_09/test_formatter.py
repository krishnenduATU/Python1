'''
Script : test_formatter
Author : Krishnendu
Purpose : To build a new test case
Usage : python -m unittest test_formatter.py
Revision History :
Aplha Version : 31-Oct-2022
Tested : Windows-10-10.0.22621-SP0 with Python version 3.10.7
Notes : Calls formater.py
'''
import unittest 
import formater

# Defines a new test case class called TestFormatter, which inherits from unittest.TestCase
class TestFormatter(unittest.TestCase):
    # Defines a test method: check for lower case
    def test_lower(self):
        test_text = "KRISHNENDU"
        result = formater.convert_lower(test_text)
        # .assertEqual(a, b) is equivalent to a == b
        self.assertEqual(result, "krishnendu")
    # Defines a test method: check for upper case
    def test_upper(self):
        test_text = "krishnendu"
        result = formater.convert_upper(test_text)
        self.assertEqual(result, "KRISHNENDU")
        #self.assertEqual(result, "KrisHNENDU") >> Test will fail here

# Defines a command-line entry point, which runs the unittest test-runner .main()
if __name__ == "__main": 
    unittest.main()