# To import the math library from the Python standard libraries
# This will import all the functions in math library
import math
print("Example to import all modules from math")
print("Input lengths of the two short triangle sides:")
side_01 = float(input("Side 1 = "))
side_02 = float(input("Side 2 = "))
result = math.sqrt(side_01**2 + side_02**2)
print(f"The length of the hypotenuse to four decimal places is {(result):.4f}")
