import csv
import os

class Student:
    """Class to represent a single student with their grades"""
    def __init__(self, name):
        self.name = name
        self.grades = []
    
    def add_grade(self, grade):
        """Add a grade to the student's grade list"""
        if 0 <= grade <= 100:
            self.grades.append(grade)
            return True
        return False
    
    def calculate_average(self):
        """Calculate the average grade for the student"""
        if len(self.grades) == 0:
            return 0
        return sum(self.grades) / len(self.grades)
    
    def get_letter_grade(self, average):
        """Convert numerical average to letter grade"""
        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        else:
            return "F"
    
    def display_info(self):
        """Display student information"""
        average = self.calculate_average()
        letter = self.get_letter_grade(average)
        print(f"Name: {self.name}")
        if len(self.grades) > 0:
            print(f"Grades: {self.grades}")
            print(f"Average: {average:.1f} ({letter})")
        else:
            print("Grades: None yet")


class GradeBook:
    """Class to manage all students and their grades"""
    def __init__(self, csv_file="Students.csv"):
        self.students = {}
        self.csv_file = csv_file
        self.load_from_csv()
    
    def add_student(self, name):
        """Add a new student to the gradebook"""
        if name not in self.students:
            self.students[name] = Student(name)
            self.save_to_csv()
            return True
        return False
    
    def find_student_by_name(self, name):
        """Find a student by their name"""
        return self.students.get(name)
    
    def add_grade_to_student(self, name, grade):
        """Add a grade to a specific student"""
        student = self.find_student_by_name(name)
        if student:
            result = student.add_grade(grade)
            if result:
                self.save_to_csv()
            return result
        return False
    
    def get_all_students(self):
        """Get list of all students"""
        return list(self.students.values())
    
    def calculate_class_average(self):
        """Calculate average grade for the entire class"""
        all_grades = []
        for student in self.students.values():
            all_grades.extend(student.grades)
        
        if len(all_grades) == 0:
            return 0
        return sum(all_grades) / len(all_grades)
    
    def display_all_students(self):
        """Display all students in a formatted table"""
        if len(self.students) == 0:
            print("No students in the gradebook yet.")
            return
        
        print("Name                 Average    Grade")
        print("-" * 40)
        
        for student in self.students.values():
            avg = student.calculate_average()
            letter = student.get_letter_grade(avg)
            print(f"{student.name:<20} {avg:<10.1f} {letter:<5}")
        
        print(f"Total Students: {len(self.students)}")
    
    def display_class_summary(self):
        """Display class summary with average and student count"""
        if len(self.students) == 0:
            print("No students in the gradebook yet.")
            return
        
        class_avg = self.calculate_class_average()
        
        print(f"Total Students: {len(self.students)}")
        print(f"Class Average: {class_avg:.1f}")
    
    def save_to_csv(self):
        """Save all students and grades to CSV file"""
        try:
            with open(self.csv_file, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Name', 'Grades'])
                
                for student in self.students.values():
                    grades_str = ','.join(map(str, student.grades))
                    writer.writerow([student.name, grades_str])
        except Exception as e:
            print(f"Error saving to CSV: {e}")
    
    def load_from_csv(self):
        """Load students and grades from CSV file"""
        if not os.path.exists(self.csv_file):
            return
        
        try:
            with open(self.csv_file, 'r') as file:
                reader = csv.reader(file)
                next(reader, None)
                
                for row in reader:
                    if len(row) >= 2:
                        name = row[0].strip()
                        grades_str = row[1].strip()
                        
                        if name:
                            student = Student(name)
                            
                            if grades_str:
                                try:
                                    grades = [int(g.strip()) for g in grades_str.split(',') if g.strip()]
                                    student.grades = grades
                                except ValueError:
                                    pass
                            
                            self.students[name] = student
        except Exception as e:
            print(f"Error loading from CSV: {e}")