import math


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

def budget(): 
    base = int(input("How many budget categories do you have: "))
    total = int(input("What is your total monthly income: "))
    categories = []
    for i in range(base):
        category = input(f"Enter the name of category(ex: rent) {i + 1}: ")
        categories.append(category)
    print("Your budget categories are:", categories)
    print("enter percentage for each category: ")
    percentages = []
    for i in range(base):
        percentage = float(input(f"Enter percentages for {categories[i]}: "))
        percentages.append(percentage)

    combined = sum(percentages)
    if combined != 100:
        print("Error The total percentage must equal 100")
        return
    
def compound():
    start = int(input("what is the starting amount: "))
    percent = float(input("what is the interest reate: "))
    time = int(input("how many units of time will it be compounded for: "))
    percent = percent / 100
    final = start * (1 + percent) ** time
    fixed = round(final, 2)
    print("your amount after", time, "units of time is:", fixed)
    
def savings():
    amount = int(input("how much are you saving for: "))
    new = input(" 1 for weely 2 for monthly: ")
    mon = input('how much are you putting in each time: ')
    if new == 1:
        final1 = mon * 4
        equate = amount / mon
        print("it will take", equate, "months to save enough")
    elif new == 2:
        equate2 = amount / mon
        print ("it will take", equate2, "months to save enough")
        

print("this is a financial calculator")
choice = input("do you want to use: 1. Savings Time Calculator, 2. Compound Interest Calculator, 3. Budget Allocator, 4. Sale Price Calculator, 5. Tip Calculator. enter corresponding calculator: ")
if choice == "5":
    tip()
elif choice == "4":
    sale()
elif choice == "3":
    budget()
elif choice == "2":
    compound()
elif choice == "1":
    savings()
