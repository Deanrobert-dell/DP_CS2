import csv
import os #fpr file handling stuff

class Student:
    #class represents students with the grade
    def __init__(self, name):

        self.name = name
        self.grades = []
    
    def add_grade(self, grade):
        #Adds grade to lsit withstudent
        if 0 <= grade <= 100:
            self.grades.append(grade)

            return True
        return False
    
    def calculate_average(self):
        #averages (grades added devided bya mount)
        if len(self.grades) == 0:
            return 0
        return sum(self.grades) / len(self.grades)
    
    def lettergrade(self, average):
        #if to see what letter they have
        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "c"
        elif average >= 60:
            return "D"
        else:
            return "F" #trash
    
    def info(self):
        #this prints fhe student info
        average = self.calculate_average()
        letter = self.lettergrade(average)
        print(f"Name: {self.name}") #peak...

        if len(self.grades) > 0:
            print(f"Grades: {self.grades}")
            print(f"Average: {average:.1f} ({letter})")
        else:
            print("add grades")


class GradeBook:
    # manages students and grades z=+csv stuff
    def __init__(self, csv_file="Students.csv"):
        self.students = {}

        self.csv_file = csv_file
        self.load_from_csv()
    
    def add_student(self, name):
    #adds student to grades
        if name not in self.students:
            self.students[name] = Student(name)

            print(f"Students dict : {self.students}")
            self.save_to_csv()
            return True
        return False
        
    def search(self, name):
        #searchforthestudent
        return self.students.get(name)
    
    def add_grade_to_student(self, name, grade):
        #Gives grades to slesific student
        student = self.search(name)
        if student:
            result = student.add_grade(grade)
            if result:
                self.save_to_csv()
            return result
        
        return False
    
    def get_all_students(self):
        #list of kids
        return list(self.students.values())
    
    def All_averages(self):   #averages whole class
        
        all_grades = []
        for student in self.students.values():
            all_grades.extend(student.grades)
        
        if len(all_grades) == 0:
            return 0
        return sum(all_grades) / len(all_grades)
    
    def display_all_students(self):

        #fomats them
        if len(self.students) == 0:
            print("No studentsyet.")
            return
        
        print("Name                 Avserage    Grade")
        
        
        for student in self.students.values():
            avg = student.calculate_average()
            letter = student.lettergrade(avg)


            print(f"{student.name:<20} {avg:<10.1f} {letter:<5}")
        
        print(f"Total Students: {len(self.students)}")
    
    def classsummary(self):
        #class summary wit average"

        if len(self.students) == 0:
            print("literally no students in the gradebook yet.")
            return
        
        class_avg = self.All_averages()
        
        print(f" Students: {len(self.students)}")

        print(f" Average: {class_avg:.1f}")
    
    def save_to_csv(self):
#saves students and grades to sCSV file
        try:
            with open(self.csv_file, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Name', 'Grades'])
                
                for student in self.students.values():

                    grades_str = ','.join(map(str, student.grades))
                    writer.writerow([student.name, grades_str])
        except Exception as e:
            print(f"problem: {e}")
    
    def load_from_csv(self):
    #load students and grades form the csv
        if not os.path.exists(self.csv_file):
            return
        
        try:
            with open(self.csv_file, 'r') as file:
                reader = csv.reader(file)
                next(reader, None)
                
                for row in reader:
                    if len(row) >= 1:
                        name = row[0].strip()
                        grades_str = row[1].strip() if len(row) > 1 else "" #leaves empty without grades
                        
                        if name:
                            student = Student(name)
                            

                            if grades_str:
                                try:
                                    grades = [int(g.strip()) for g in grades_str.split(',') if g.strip()] #this is the one that was giving me problems, it splits the grades by comma and converts them to integers, while also handling any extra spaces or empty values.
                                    student.grades = grades

                                except ValueError:
                                    pass
                            
                            self.students[name] = student
        except Exception :
            print(f"messed up flowchacho: {Exception}")