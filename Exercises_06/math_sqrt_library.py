# To import only function sqrt from the math package
from math import sqrt
print("Import only function sqrt from math")
print("Input lengths of the two short triangle sides:")
side_01 = float(input("Side 1 = "))
side_02 = float(input("Side 2 = "))
result = sqrt(side_01**2 + side_02**2)
print(f"The length of the hypotenuse to four decimal places is {(result):.4f}")