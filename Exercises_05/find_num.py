def find_num(number_list: list, number: int): 
    for iterate_number in number_list: 
        if iterate_number == number: 
            return True 
        else: 
            pass 
    # Below step will make function to return False instead of None if the value is not found    
    return False        
result = find_num([1,2,3,4,5,6,7,8,9], 9) 
print(f"When number 9 is in list > {result}")
result = find_num([1,2,3,4,5,6,7,8], 9) 
print(f"When number 9 is not in list > {result}")