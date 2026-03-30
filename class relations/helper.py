class Students:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def summary(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def display(self):
        print(f"Student: {self.name}")
        print(f"Grades: {self.grades}")
        print(f"Average: {self.summary()}")


class GradeBook:
    def __init__(self):
        self.students = []

    def make_student(self, student):
        self.students.append(student)

    def get_student(self, name):
        for student in self.students:
            if student.name == name:
                return student
        return None

    def view(self):
        for student in self.students:
            student.display()
    def st_records(self, student): #display all students grades
        student.display()
