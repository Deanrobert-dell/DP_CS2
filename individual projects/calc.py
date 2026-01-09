import math
import turtle
def save():

def interest():

def budget():

def sale():

def tip():
    bill = input("what is the price of item your buying: ")
    tip = input("what percentage are you tipping: ")
    tipp = 1+(tip/100)
    final = bill * tipp
tip()

print("this is a financial calculator")
choice = input("do you want to use: 1. Savings Time Calculator, 2. Compound Interest Calculator, 3. Budget Allocator, 4. Sale Price Calculator, 5. Tip Calculator. enter corresponding calculator: ")
if choice == 1:
    tip()