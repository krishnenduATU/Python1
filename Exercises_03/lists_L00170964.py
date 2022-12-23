'''
Script: list_L00170964.py
By: L00170964
Purpose: To demostrate usage of lists and it's methods in python
Prerequisites: Read lecturer note "Walkthroughs - 3. Data Structures"
Tested: on Python v3.10.7 under Windows 11
Revision History:
Alpha version: 27SEPT22
Notes:
List items are ordered, mutable, and allow duplicate values. Different
list methods are explained in this script.
'''
# Create list
list_01 = [1,2,3,4,"A", "UVW"]
list_02 = [5,6,7,8,9,"B", "XYZ"]
# Lenght of list
list_len = len(list_01)
print("List 1 contains : ", list_01)
print("List 2 contains : ", list_02)
print("Lenght of List 1 : ", list_len)
# Below method directly prints length without storing in a vairable
print("Lenght of List 2 : ", len(list_02))
print("Slicing 2nd & 3rd character from List 1 : ", list_01[1:3:1])
print("Slicing last character from List 1 : ", list_01[-1])
# Concatenate lists
concatenate_list = list_01 + list_02
print("Concatenate Lists 1 & 2 : " , concatenate_list)
# Nested lists
nested_list = [list_01,list_02]
print("Nested List : ", nested_list)
# Lists are mutable, items may be indexed and selectively edited
list_01[2] = "Python"
print("Updating value of item 2 on List 1 : ", list_01)
# Methods of list objects
# To append a item to list
list_01.append("Linux")
print("Append item to List 1 : ", list_01)
# To insert a item to a given position
list_01.insert(3,"Is Fun")
print("Insert a item at index 3 on List 1 : ", list_01)
# To return the number of times a particular item appears in the list
list_01_count = list_01.count('A')
print("Count number of times \"A\" appears in the List 1 : ",list_01_count)
# To return index of the item
print("Index of item Linux in List 1 : ", list_01.index('Linux'))
# To copy list 
list_03 = list_01.copy()
print("Copying items from List 1 to List 3 : ",list_03)
# To remove item at the given position in the list, by default removes last item in list
list_01.pop()
print("Pop last item from List 1", list_01)
list_01.pop(3)
print("Pop item on position 3 from List 1", list_01)
# To reverse the elements in list
list_01.reverse()
print("Reverse List 1", list_01)
# To remove all items from the list
list_01.clear()
print("List 1 removed : ",list_01)
