# Function will return boolean True if remainder is 0 when first operand is divided by the second
def divisible(numerator: int, denominator: int)->bool: 
    return numerator % denominator == 0 

print(f"Is 32 divisible by 4 : {divisible(32,4)}")
print(f"Is 29 divisible by 4 : {divisible(29,4)}")


