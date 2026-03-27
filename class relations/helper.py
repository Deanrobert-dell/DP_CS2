class Students:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def get_average(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def display(self):
        print(f"Student: {self.name}")
        print(f"Grades: {self.grades}")
        print(f"Average: {self.get_average()}")


class GradeBook:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def get_student(self, name):
        for student in self.students:
            if student.name == name:
                return student
        return None

    def display_all(self):
        for student in self.students:
            student.display()