
# When break is used, loop exits after first match
# Here, the variable contains two "n"
print("Testing break control statements")
for break_letter in "Krishnendu" :
    if break_letter == "n":
        print("Yes, we got the letter ",break_letter)
        break
    else:
        print("Sorry, didn't find letter ",break_letter)

# When continue is used, loop exits only after it iterate via all items
print("Testing continue control statements")
for continue_letter in "Krishnendu":
    if continue_letter == "n":
        print("Yes, found the letter ",continue_letter)
        continue
    else:
        print("Sorry, didn't find letter ",continue_letter) 

# Pass does nothing, generally used as a placeholder
print("Testing pass control statements")
for pass_letter in "Krishnendu":
    if pass_letter == "n":
        print("Yes, found the letter ",pass_letter)
        pass        
    else:
        print("Sorry, didn't find letter ",pass_letter)

my_list = [1,2,3,0] 
for my_number in my_list: 
    if my_number == 1: 
        pass 
    if my_number == 2: 
        continue 
    if my_number == 3: 
        print(f"Found the number {my_number}") 
    if my_number == 0: 
        break
