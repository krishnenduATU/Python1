'''
Script: exercise_project_l00170964.py
By: L00170964
Purpose: To demostrate the use of python packages
Usage : python exercise_project_l00170964.py
Tested: on Python v3.10.7 under Windows 11
Revision History:
Alpha version: 04OCT22
Notes:
Packages are collection of modules, here folder Exercises_06\l00170964_library
contains modules square_module and cube_module 
'''
# Import package
import l00170964_library
# Global variable from __init__.py
print(l00170964_library.copyright)
input_num = int(input("Enter a number : "))
# Modules square_module and cube_module are already imported in __init__.py file, so function is used directly
print(f"Square of {input_num} = {l00170964_library.square_number(input_num)}")
print(f"Cube of {input_num} = {l00170964_library.cube_number(input_num)}")

# Calling text functions from cube & square modules
l00170964_library.cube_text()
l00170964_library.square_text()