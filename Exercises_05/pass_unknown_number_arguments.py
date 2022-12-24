# Asterisk symbol * is used to pass unknown number of arguments 
def auto_adder(*number):
    sum = 0
    for num in number:
        # sum = sum + number
        sum += num
    return sum
result = auto_adder(1,2,3,4,5) 
print("Sum of numbers : ",result)
