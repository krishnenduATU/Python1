'''
Script : validate_user_input
Author : Krishnendu
Purpose : To validate user input
Usage : python validate_user_input.py
Revision History :
Aplha Version : 23-Oct-2022
Tested : Windows-10-10.0.22621-SP0 with Python version 3.10.7
Notes : Test case to check user input is as per requirement or not
'''
# Import modules 
# Functions
def validate_integer():
    while True:
        try:
            user_input = int(input("Enter a integer value : "))
        except:
            print("General Error ..") 
            continue
        else:
            print(f"The value entered is {user_input}")
            return True            
        finally:
            print("Finished ")
# Variables 
# Main code
validate_integer()




