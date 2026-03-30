from helper import *
from faker import Faker

fake = Faker()
print(fake.name())

def display_menu():
    #displays the main menu
    print(" Grade Book ")
    print("1 Create new student") #makes a student
    print("2 add grade to student") #gives student a grade
    print("3 view student records") #shows student records???
    print("4 view all students") #shows students and grades
    print("5 clas summary") #averages grades
    print("6 QUIT") #leaves program


def main():
    students = []  # store shapes
    
    while True:
        display_menu()
        choice = input("Enter student name: ").strip()
        


#all the formulas details from helper
        elif choice == "1":
            make_student(student)

        elif choice == "2":
            add_grade(student)

        elif choice == "3":
            st_records(student)

        elif choice == "4":
            view(student)

        elif choice == "5":
            summary(student)

        elif choice == "6":
            print("beebye")
            break
        else:
            print("Invalid choice do a 1 or 6, do'nt be stupid.")


main()