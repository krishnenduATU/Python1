'''
Script: Tuple_L00170964.py
By: L00170964
Purpose: To demostrate usage of tuple in python
Prerequisites: Read lecturer note "Walkthroughs - 3. Data Structures"
Tested: on Python v3.10.7 under Windows 11
Revision History:
Alpha version: 28SEPT22
Notes:
Tuples are immutable i.e. cannot remove/append/update items in a tuple.
'''
list_01 = [1,2,3,"one", "two"]
# Create tuple
tuple_01 = (1,2,3,"one","two","three","ABC","ABC")
tuple_02 = (4,5,6,"Six","Seven")
print("Type of list_01 : ", type(list_01))
print("Type of tuple_01 : ", type(tuple_01))
# How many times a item appears in a tuple
print("Counting item ABC in tuple : ",tuple_01.count("ABC"))
# To find the index of the given item
print("Index of \"one\" in tuple : ",tuple_01.index("one"))
# To print last item of the tuple
print("Last item in tuple : ",tuple_01[-1])
# To print iteams based on index range
print("Print range of items in tuple : ",tuple_01[2:5])
# Concatenate tuple
concatenate_tuple = tuple_01 + tuple_02
print("Concatenate tuple : ",concatenate_tuple)
# To confirm tuples are immutable. Below line will throw TypeError
tuple_01[1] = "Python"


