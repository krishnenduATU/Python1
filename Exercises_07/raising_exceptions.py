'''
Script : raising_exceptions
Author : Krishnendu
Purpose : To demostrate usage of Raising Exceptions
Usage : python raising_exceptions.py
Revision History :
Aplha Version : 23-Oct-2022
Tested : Windows-10-10.0.22621-SP0 with Python version 3.10.7
Notes : To raise an exception when validating input
'''
# Import modules 
# Functions 
# Variables 
user_input = int(input("Enter a integer greater than 0 : "))
# Main code
if user_input <= 0:
    raise Exception("Value must be greater than 0")
else: 
    print("Validation checks passed")