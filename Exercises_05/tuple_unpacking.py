'''
Script: most_expensive.py
By: L00170964
Purpose: To find which product is most expensive in a list
Prerequisites: Read lecturer note "Walkthroughs - 5. Functions"
Tested: on Python v3.10.7 under Windows 11
Revision History:
Alpha version: 04OCT22
Notes:
To find out which item in a list is most expensive. Here, list containts
prices of fruit from the supermarket
'''
def most_expensive(price_list):
   max_price = 0
   max_price_item = ""
   for item,price in price_list:
    if price > max_price:
        max_price = price
        max_price_item = item
    else:
        pass 
   return max_price_item,max_price
price_list = [("Pineapple", 1.0), ("Apples", 1.5), ("Pears", .7), ("Peaches", .8)]
product, price = most_expensive(price_list)
print("Product List : ",price_list)
print(f"Product {product} of price {price} is most expensive in the list")