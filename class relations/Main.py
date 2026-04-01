from helper import GradeBook

gradebook = GradeBook("Students.csv")

def display_menu():
    """Display the main menu"""
    print("GRADE BOOK")
    print("1 Create new student")
    print("2 Add grade to student")
    print("3 View student records")
    print("4 View all students")
    print("5 Class summary")
    print("6 QUIT")

def add_student_menu():
    """Handle adding a new student"""
    name = input("Enter student name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return
    
    if gradebook.add_student(name):
        print(f"Student {name} added successfully.")
    else:
        print(f"Student {name} already exists.")
    
    input("Press Enter to continue...")

def add_grade_menu():
    """Handle adding a grade to a student"""
    students = gradebook.get_all_students()
    if len(students) == 0:
        print("No students in the gradebook yet.")
        input("Press Enter to continue...")
        return
    
    print("Current Students:")
    for student in students:
        print(f"- {student.name}")
    
    name = input("Enter student name: ").strip()
    student = gradebook.find_student_by_name(name)
    
    if not student:
        print(f"Student {name} not found.")
        input("Press Enter to continue...")
        return
    
    try:
        grade = int(input("Enter grade (0-100): "))
        
        if grade < 0 or grade > 100:
            print("Grade must be between 0 and 100.")
            input("Press Enter to continue...")
            return
        
        if gradebook.add_grade_to_student(name, grade):
            avg = student.calculate_average()
            letter = student.get_letter_grade(avg)
            print(f"Grade added. {name} average: {avg:.1f} ({letter})")
        else:
            print("Error adding grade.")
    
    except ValueError:
        print("Invalid grade. Please enter a number between 0 and 100.")
    
    input("Press Enter to continue...")

def view_student_record():
    """Handle viewing a specific student's record"""
    students = gradebook.get_all_students()
    if len(students) == 0:
        print("No students in the gradebook yet.")
        input("Press Enter to continue...")
        return
    
    print("Available Students:")
    for student in students:
        print(f"- {student.name}")
    
    name = input("Enter student name: ").strip()
    student = gradebook.find_student_by_name(name)
    
    if student:
        student.display_info()
    else:
        print(f"Student {name} not found.")
    
    input("Press Enter to continue...")

def view_all_students():
    """Handle viewing all students"""
    gradebook.display_all_students()
    input("Press Enter to continue...")

def class_summary():
    """Handle displaying class summary"""
    gradebook.display_class_summary()
    input("Press Enter to continue...")

def main():
    """Main function to run the grade book system"""
    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()
        
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
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")
            input("Press Enter to continue...")

if __name__ == "__main__":
    main()