'''
Script: even_number.py
By: L00170964
Purpose: To find if list contains even numbers or not
Usage: python even_number.py
Tested: on Python v3.10.7 under Windows 11
Revision History:
Alpha version: 04OCT22
Notes:
Function "even_number" will return True if even number is present in
the passed list, else will return "None". 
'''


# Function to check if list contains even number's
def even_number(number_list):
    for num in number_list:
        # Check if number is even number or not
        if num % 2 == 0:
            return True
        else:
            pass
    # If below step is commented, function will return "None"
    return False 
# Below list contains even numbers
number_list = [1,7,5,9,4,6,5]
result = even_number(number_list)
print(f"List {number_list} contains even numbers ? : {result}")
# Below list doesn't contains even numbers
number_list = [1,7,5,9,11]
result = even_number(number_list)
print(f"List {number_list} contains even numbers ? : {result}")