'''
Script: dictionary_L00170964.py
By: L00170964
Purpose: To demostrate usage of dictionary data structure in python
Prerequisites: Read lecturer note "Walkthroughs - 3. Data Structures"
Tested: on Python v3.10.7 under Windows 11
Revision History:
Alpha version: 28SEPT22
Notes:
Dictionaries are unordered structures for storing objects. They are in key-pair
format, which uniquely identifying each entry, without needing to know its location. 
'''
# Create & print dictionary
student = {"fname":"Krish",'sname':'VP','course':'MSc Cloud Computing'}
print("Student dictionary : ",student)
print("Keys in student dictionary : ",student.keys())
print("Values in student dictionary : ",student.values())
print("Items in student dictionary : ",student.items())
# Print value for key
print(f"{student['fname']} is studying {student['course']}")
# Add a key-value pair
student['duration'] = 'Full-time'
print("Adding new key-value to student dictionary : ",student)
# Get method
print(f"{student['fname']} is studying {student['course']} and it is {student.get('duration')} course")
# Update value
student['duration'] = 'Part-time'
print("Update value for duration key : ",student)
# Copy dictionary
student_copy = student.copy()
print("Student copy dictionary : ",student_copy)
# Clear dictionary
student.clear()
print("Student dictionary after clear method: ",student)
