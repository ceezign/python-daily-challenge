# A student class grade

class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        if 0 <= grade <= 100:
            self.grades.append(grade)
        else:
            raise ValueError("Grade must be between 0 and 100")

    def average(self):
        if not self.grades:
            return 0.00
        return round(sum(self.grades) / len(self.grades), 2)

    def status(self):
        return "Pass" if self.average() >= 60 else "Fail"

    def __str__(self):
        return f" Student: {self.name} (Average: {self.average()}) "

stud1 = Student("Alice")
stud1.add_grade(75)
stud1.add_grade(88)
stud1.add_grade(58)

print(stud1)
print("Grades:", stud1.grades)
print("Status: ", stud1.status())

stud2 = Student("Bob")
stud2.add_grade(50)
stud2.add_grade(60)
print(stud2)
print("Status:", stud2.status())