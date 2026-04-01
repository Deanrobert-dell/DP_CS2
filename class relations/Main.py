from helper import GradeBook #just need this class contains functions
import os


gradebook = GradeBook("class relations/Students.csv") #path

def display_menu():
    #main menu
    print("GRADE B0OK")
    print("1 Create new student")

    print("2 Adds grade to student")
    print("3 View student records")

    print("4 View aLll students")
    print("5 class summary")

    print("6 QUIT")

def add_student_menu():
    #Take func to make student
    name = input("entera  student name: ").strip()
    if not name:
        print("") #idiot proof
        return
    
    if gradebook.add_student(name):
        print(f"Student {name} added successfully.")
    else:
        print(f"Student {name} already exists snupid.")
    
    input("ENTER")

def add_grade_menu():
    #Handle adding a grade to a student
    students = gradebook.get_all_students()
    if len(students) == 0:

        print("No students in the gradebook yet.makesome")
        input("ENTER")
        return
    
    print("current Students:")
    for student in students:
        print(f"- {student.name}") #crazy format method!!!
    
    name = input("Enter student name: ").strip()
    student = gradebook.search(name)
    
    if not student:
        print(f" Student {name} not found.")
        input("ENTER")
        return
    
    try:
        grade = int(input("enter grade (0-100): "))


        
        if grade < 0 or grade > 100:
            print("Grade must be between 0 and 100.")
            input("ENTER")
            return
        
        if gradebook.add_grade_to_student(name, grade):
            avg = student.calculate_average()
            letter = student.lettergrade(avg)

            print(f"Grade added. {name} average: {avg:.1f} ({letter})")
        else:
            print("Error adding grade.")
    
    except ValueError:
        print("plurt to 0-100")
    
    input("ENTER")

def view_student_record():
    #first student viewing stuff
    students = gradebook.get_all_students()
    if len(students) == 0:

        print("No students in the gradebook yet.")
        input("ENTER")
        return
    
    print("pick one :")
    for student in students:
        print(f"- {student.name}") #method...
    
    name = input("Enter student name: ").strip()
    student = gradebook.search(name)
    
    if student:
        student.info()
    else:
        print(f"Student {name} not found.")
    
    input("ENTER")

def view_all_students():
    #student viewing 

    gradebook.display_all_students()
    input("ENTER")

def class_summary():
    #sumamry
    gradebook.classsummary()
    input("ENTER")

def main():
    #main gardebook func
    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()
         # all the choices ever
        if choice == "1":
            add_student_menu()
        
        elif choice == "2":
            add_grade_menu()
        
        elif choice == "3":
            view_student_record()

        
        elif choice == "4":
            view_all_students()
        
        elif choice == "5":
            class_summary()
        
        elif choice == "6":

            print("beebye")
            break
        
        else:
            print("pluh, 1-6")
            input("ENter")

if __name__ == "__main__": #runs only When not imported froma anohtne file
    main()