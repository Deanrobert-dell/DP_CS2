from helper import *
import csv

def display_menu():
    #displays the main menu
    print(" Grade Book ")
    print("1 Create new student") #makes a student
    print("2 add grade to student") #gives student a grade
    print("3 view student records") #shows student records???
    print("4 view all students") #shows students and grades
    print("5 class summary") #averages grades
    print("6 QUIT") #leaves program

        


#all the formulas details from helper
def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            make_student(student) #make name for student, added to csv
           

        elif choice == "2":
            add_grade(student) #give a grade to individual student

        elif choice == "3":
            st_records(student) #individual student grades

        elif choice == "4":
            view(student) #shows all students and grades

        elif choice == "5":
            summary(student) #average of all class grades

        elif choice == "6":
            print("beebye")
            break
        else:
            print("Invalid choice do a 1 or 6, don't be stupid.")


main()