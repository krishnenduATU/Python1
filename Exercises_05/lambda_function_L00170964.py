'''
Script: lambda_function_L00170964.py
By: L00170964
Purpose: To demostrate the usage of lambda in python
Prerequisites: Read lecturer note "Walkthroughs - 5. Functions"
Tested: on Python v3.10.7 under Windows 11
Revision History:
Alpha version: 04OCT22
Notes:
Lambda is similar to function which doesn't have a name and are
usally used as single-use function 
'''
# lambda arguments : expression
circumference = lambda radius : 2 * 3.142 * radius 
area = lambda radius : 3.142 * radius * radius 
radius = int(input("Enter the raidus of circle : "))
print(f"Circumference of circle = {circumference(radius):.2f}\nArea of circle = {area(radius)}")