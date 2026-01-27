#DP 2nD pass gen
#import random and string for ascii cases
import random
import string
#function for asking for cases
def generate_passwords():
    length = int(input("How long does the password need to be: "))

    lower = input("Does the password need lowercase letters (Y/N): ").upper()
    upper = input("Does the password need uppercase letters (Y/N): ").upper()
    numbers = input("Does the password need numbers letters (Y/N): ").upper()
    special = input("Does the password need special characters letters (Y/N): ").upper()

    chars = ""
#multipe if statements or asking cases
    if lower == "Y":
        chars += string.ascii_lowercase
    if upper == "Y":
        chars += string.ascii_uppercase
    if numbers == "Y":
        chars += string.digits
    if special == "Y":
        chars += string.punctuation

    print("osisible Passwords:\n")
#print multiple passwords from for loop shosing from charachters
    for i in range(4):
        password = ""
        for j in range(length): #have it go for ho long shosen length is
            password += random.choice(chars)
        print(password)
#main function (so it can loop)
def main():
    print("elcome to a password generator")

    while True:
        print("\nMaIN MENU:")
        print("Type the number for the action you would like to perform 1 orr 2")
        print("1. Gen. Passwords")
        print("2. Exit")

        choice = input("Choice: ")
#exit or run pass gen
        if choice == "1":
            generate_passwords()
        elif choice == "2":
            print("beebye!")
            break
        else:
            print("invalid choice, try again.")

main()
