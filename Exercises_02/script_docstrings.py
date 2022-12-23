'''
Script: script_docstring.py
By: L00170964
Purpose: To demostrate use of comments and docstring in script
Prerequisites: Read lecturer note "Walkthroughs - 2. Documentation"
Tested: on Python v3.10.7 under Windows 11
Revision History:
Alpha version: 06OCT22
Notes:
A programme that takes input from a user and calls function hello_user to print
a Hello message.
'''
# Single line comments begins with the # sign
# For multi-line comments use '''Documentations ''' 

# This function accepts a string argument and return a string
def hello_user(name:str)->str:
    print(f"Hello {name}")

# Takes string user input 
input_name = str(input("Enter Your Name : "))
# Calls the function "hello_user"
hello_user(input_name)