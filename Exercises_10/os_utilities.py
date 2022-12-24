'''
Script : os_utilities.py
Author : Krishnendu VP
Purpose : To get OS platform 
Usage : python os_utilities.py
Revision History :
Aplha Version : 22-Oct-2022
Tested : Windows-10-10.0.22621-SP0 with Python version 3.10.7
Notes : 
'''
# Import modules
import os, platform
import psutil

# Functions 
def detect_os()->str:
    return platform.system() # Returns OS name

def cpu_load():

    return(psutil.cpu_count(), psutil.cpu_percent()) # Returns CPU metrics
# Variables  
#def currect_os()->str:
os_platform = platform.system()
os_platform = os_platform.lower()

# Main code
if (__name__ == '__main__'): 
    print(f"This module executes as a standalone script")
    if os_platform == "windows":
        print("You are working in a Windows OS !!!")
    elif os_platform == "linux":
        print("You are working in a Linux OS !!!")
    elif os_platform == "darwin": 
        print("Your Apple system is MacOS") 
    elif os_platform == "cygwin": 
        print("Your Apple system is MacOS") 
    elif os_platform == "aix":
        print("Your IBM system is AIX")
    else:
         print(f"Cannot continue, unidentified system = {os_platform}")
         sys.exit()

else:
    pass 
    
    #print(f"This module is called {__name__} and is being called by another script")
    