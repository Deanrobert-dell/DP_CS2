import math
import turtle
"""def save():

def interest():

def budget():"""

def sale():
    price = int(input("what is the original price of the item: "))
    sale = int(input("what percentage is the discount: "))
    discount_amount = (sale/100) * price
    final_price = price - discount_amount
    fixed = round(final_price, 2)
    print(fixed)

def tip():
    bill = int(input("what is the price of item your buying: "))
    tip = int(input("what percentage are you tipping: "))
    tipp = 1+(tip/100)
    final = bill * tipp
    fixed = round(final, 2)
    print(fixed)


print("this is a financial calculator")
choice = input("do you want to use: 1. Savings Time Calculator, 2. Compound Interest Calculator, 3. Budget Allocator, 4. Sale Price Calculator, 5. Tip Calculator. enter corresponding calculator: ")
if choice == "5":
    tip()
elif choice == "4":
    sale()