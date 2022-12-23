'''
Script: character_slicing.py
By: L00170964
Purpose: To demostrate character slicing in python.
Prerequisites: Read lecturer note "Walkthroughs - 1. Assignments and Variables"
Tested: on Python v3.10.7 under Windows 11
Revision History:
Alpha version: 26SEPT22
Notes:
A programme to slice strings in python
'''
string = "Greetings"
print("Value of string : ", string)
# To extract characters from the string, in the format [start:stop:step]
print("Slicing first four characters : ", string[0:4:1])
# Reverse indexing example
print("Slicing last four character : ", string[-1:-5:-1])
# To grab a single character 
print("Slicing sixth character : ", string[5])
# Slice the string and reassemble a new string with changes
string = "Krishnendu P"
print(f"Value of string : {string}")
first_letters = string[0:5:1]
last_letters = string[-1]
insert_letters = "V"
new_string = first_letters + insert_letters + last_letters
print(f"New string after reassembling : {new_string}")
# Example to demostrate string and a number are of different types
first_character = "1"
second_character = "2"
new_character = first_character + second_character
print(f"Value when 1 & 2 are passed as strings : {new_character}")
first_number = 1
second_number = 2
new_number = first_number + second_number
print(f"Value when 1 & 2 are passed as integers : {new_number}")
