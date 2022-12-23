'''
Script: set_L00170964.py
By: L00170964
Purpose: To demostrate usage of set data structure in python
Prerequisites: Read lecturer note "Walkthroughs - 3. Data Structures"
Tested: on Python v3.10.7 under Windows 11
Revision History:
Alpha version: 28SEPT22
Notes:
Sets cannot have two items with the same value. Duplicate values will 
be ignored. Cannot access items in a set by referring to an index or a key. 
'''
set_1 = {"one","two","three",4,5,6}
set_2 = {"A","B","C",10,11,12,4,5,6}
print("Type of set_1 : ",type(set_1))
# Print set
print("Set 1 contains : ",set_1)
print("Set 2 contains : ",set_2)
# Add to set
new_item = set_1.add("ABC")
print("Append \"ABC\" to set : ",set_1)
# Remove an item in a set
remove_item = set_1.remove("ABC")
print("Removed \"ABC\" from set : ",set_1)
# Check item is present in the set, returns boolean
find_item = "two" in set_1
print("Check if item \"two\" is in set : ",find_item)
# Check item is not in the set, returns boolean
find_item = "two" not in set_1
print("Check if item \"two\" is not in the set : ",find_item)
# Return a new set with all items from both sets
union_set = set_1.union(set_2)
print("Union set : ",union_set)
# Return a set containing the difference between sets
diff_set = set_1.difference(set_2)
print("Difference set : ",diff_set)
# To copy set 
set_3 = set_1.copy()
print("Copy set 1 to set 3 : ",set_3)
# Clear set
set_3.clear()
print("Remove set 3 : ",set_3)