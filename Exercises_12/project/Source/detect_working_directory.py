'''
Script : detect_working_directory
Author : Krishnendu VP
Purpose : To get OS platform and print current working directory
Usage : python detect_working_directory.py
Revision History :
Aplha Version : 22-Oct-2022
Tested : Windows-10-10.0.22621-SP0 with Python version 3.10.7
Notes : Walkthroughs - 7. Handling Errors here
'''
# Import modules
import os, platform
# Functions 
def detect_os()->str:
    return platform.system()
def detect_working_directory()->str:
    return os.getcwd()
# Variables  
current_working_directory = None
currect_os = detect_os()
currect_os = currect_os.lower()
current_working_directory = detect_working_directory()
# Main code
if (__name__ == '__main__'): 
    print(f"This module executes as a standalone script")
    if currect_os == "windows":
        print("You are working in a Windows OS !!!")
    elif currect_os == "linux":
        print("You are working in a Linux OS !!!")
    else:
         print(f"Cannot continue, unidentified system = {currect_os}")
         sys.exit()

    print(f"You are coding in directory {current_working_directory}")

else: 
    print(f"This module is called {__name__} and is being called by another script")