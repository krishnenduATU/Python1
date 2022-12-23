'''
Script: python_style_guide.py
By: L00170964
Purpose: To quickly create a python file with docstrings
Prerequisites: Read lecturer note "Walkthroughs - 2. Documentation"
Tested: On Python v3.10.7 under Windows 11
Revision History:
Alpha version: 09-OCT-2022
Notes:
Best practices that ought to be followed while writing scripts, 
such as the appropriate use of comments, variable names, and docstrings
is automated by this script. This script takes input from user and creates a .py file
with the above details.
'''
# Import standard libraries requried to create file,check directory path
import os, os.path, datetime,platform,sys

# Variables
script_name = str(input("Enter the Python script name : "))
script_author = str(input("Enter the script author : ") or "Krishnendu")
script_purpose = str(input("Enter the purpose of this script : ") or "")
script_usage = str(input(f"Enter the script usage : ") or "python '{script_name}'.py")
script_notes = str(input("Enter the script notes if any : ") or "")

# Variables for each lines
script_line = "'''\nScript : " + script_name + '\n'
author_line = 'Author : ' + script_author + '\n'
purpose_line = 'Purpose : ' + script_purpose + '\n'
usage_line = 'Usage : ' + script_usage + '\n'
# To get date in format 09-Oct-2022
version_line = "Revision History :\nAplha Version : "  + datetime.datetime.now().strftime("%d-%b-%Y")
# To get OS & python version details
os_details = "\nTested : " + platform.platform() + " with Python version " + platform.python_version()
notes_line = '\nNotes : ' + script_notes + '\n' + "'''"
var_funtions_line = "\n# Import modules \n# Functions \n# Variables \n# Main code"
doc_string = script_line,author_line,purpose_line,usage_line,version_line,os_details,notes_line,var_funtions_line
# Directory permission
mode = 0o666
directory = "C:\\Python\\" # New scripts will be created under C:\Python
# Checks if directory exists if not creates it
if not os.path.exists(directory):
    os.mkdir(directory, mode)
os.chdir("C:\\Python\\")
# Writes to the file script_name.py
with open(script_name + '.py', 'w') as f:
    f.writelines(doc_string) # To add multi-lines to file, this method writes the items of a list to the file
