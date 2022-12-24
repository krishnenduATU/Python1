'''
Script : create_directoy
Author : Krishnendu VP
Purpose : To create a directory
Usage : python create_directoy.py
Revision History :
Aplha Version : 22-Oct-2022
Tested : Windows-10-10.0.22621-SP0 with Python version 3.10.7
Notes : To systematically handle errors
'''
# Import modules
from genericpath import isdir
import os, platform
# Functions 
def detect_working_directory()->str:
    return os.getcwd()

def create_directory(dir_name:str)->int:
    # To check directory exists or not
    if os.path.isdir(dir_name):
        return 2
    else:
        try:
            os.mkdir(dir_name) # Creates directory
            return 0
        except:
            print(f"Error creating directory {dir_name}")
            return 1
# Variables  
current_working_directory = detect_working_directory()

# Main code
if (__name__ == '__main__'): 
    print(f"This module executes as a standalone script")
    dir_name = str(input("Enter directory name to create : "))
    if create_directory(dir_name) == 0:
        print(f"Creating a directory worked, location {current_working_directory}\{dir_name}")
    elif create_directory(dir_name) == 1:
        print("You couldn't create a directory!")
    elif create_directory(dir_name) == 2:
        print(f"Directory {dir_name} already exists")
else: 
    print(f"This module is called {__name__} and is being called by another script")