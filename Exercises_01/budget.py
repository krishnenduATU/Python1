'''
Script: budget.py
By: L00170964
Purpose: To calculate semester budget and total expense.
Prerequisites: Read lecturer note "Walkthroughs - 1. Assignments and Variables"
Tested: on Python v3.10.7 under Windows 11
Revision History:
Alpha version: 26SEPT22
Notes:
A programme that takes input from a student and calculates monthly expenses and 
checks if student budget meets expenses.
'''

print("Python Program To Calculate Semester Budget !!")
print("All expenses are calculated based on Euro's per month !!")
# Set default value = 0 else it will throw error if no value is given by user
budget = int(input("Enter Your Budget : "))
tution_fee = int(input("Tuition Fee: ") or 0)
rent = int(input("House Rent: ")or 0)
transport = int(input("Transportation Charges: ")or 0)
food = int(input("Food (Groceries & Eating Out): ")or 0)
mobile = int(input("Mobile & Internet Charges: ")or 0)
other_exp = int(input("Non-Essential Expenses: ")or 0)
total_exp = tution_fee + rent + transport + food + mobile
print("Total Expense :", total_exp,"Euro")
if total_exp > budget:
    print("Your expense is more than budget by ", total_exp - budget,"Euro" )
elif total_exp == budget:
    print("You are safe, expenses meets budget !!")
else:
    print("Your expenses are under the budget, you saved", budget - total_exp,"Euro" )
