'''
Script: double_number_using_map.py
By: L00170964
Purpose: To demostrate the usage of map in python
Prerequisites: Read lecturer note "Walkthroughs - 5. Functions"
Tested: on Python v3.10.7 under Windows 11
Revision History:
Alpha version: 04OCT22
Notes:
Here, a list of number is passed via map to a simple function which
doubles the values in it.
'''
# Type Hints, passing int type and returns int
def double_number(n: int)->int:  
    return n+n 
# Create a list of numbers for testing 
number_list = [1,2,3,4,5] 
# Map my_numbers to the double_number function, return type is map 
double_number_list = map(double_number, number_list) 
# Print a list of the map 
print("Double Number List using map : ",list(double_number_list)) 
# Or iterate through it 
print("Using For loop")
for item in map(double_number, number_list): 
    print(item)