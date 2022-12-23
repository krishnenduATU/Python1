'''
Script: string_manipulation.py
By: L00170964
Purpose: string manipulation in python
Prerequisites: Read lecturer note "Walkthroughs - 1. Assignments and Variables"
Tested: on Python v3.10.7 under Windows 11
Revision History:
Alpha version: 27SEPT22
Notes:
A programme to demostrate string manipulation in python.
'''
# Concatenate strings
print("Exercise to concatenate strings")
text = "Would you like brekkie ? "
print("Good Morning, Krish !! " + text)
# Use of “f” strings or formatted strings
number = 5555
divisor = 24
result = number / divisor
print(f"Result of {number} divided by {divisor} is {result:.3f}")
# Escape Sequences
print("Exercise to remove escap sequences")
print("Good Morning, \t Krish !! ")
print("Would you like brekkie ? \n")
print("Good Morning, Krish !! ", end = " ")
print("Would you like brekkie ? ")
# To determine length of a string
string = "Would you like brekkie ? "
print(f"Length of string \"{string} \"", len(string))
# String constants
orginal_string = "Hello, we are testing common string functions"
upper_string = orginal_string.upper()
lower_string = orginal_string.lower()
print("Original string : ", orginal_string)
print("Upper case : ", upper_string)
print("Lower case : ", lower_string)
print("Title case : ", orginal_string.title())
# Returns the string by converting all the characters to their opposite letter case( uppercase to lowercase and vice versa)
print("Swap case  : ", orginal_string.swapcase())
# Returns a copy of the string with leading characters stripped
print("Remove \"He\" using lstrip string : ", orginal_string.lstrip('He'))
# Method to remove leading and the trailing characters
website = 'https://www.atu.ie/'
print(f"Stripping domain name from {website} : ", website.strip('whtps:/.'))
# To replaces each matching occurrence
replace_string = "I love windows !"
print(f"Replace windows with linux in \"{replace_string} \" : ", replace_string.replace('windows', 'linux'))
