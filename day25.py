# Student Grades Project
class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        if 0 <= grade <= 100:
            self.grades.append(grade)
        else:
            print("invalid grade. enter a number between 0 and 100")

    def cal_average(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def letter_grade(self):
        avg = self.cal_average()
        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 55:
            return "C"
        elif avg >= 40:
            return "D"
        elif avg >= 30:
            return "E"
        else:
            return "F"

    def highest_and_lowest(self):
        if not self.grades:
            return None, None
        return max(self.grades) , min(self.grades)

    def display_report(self):
        avg = self.cal_average()
        letter = self.letter_grade()
        high, low = self.highest_and_lowest()
        print(f"\nGrade Report for {self.name}")
        print(f"Grade: {self.grades}")
        print(f"Average: {avg:.2f}")
        print(f"Letter Grade {letter}")
        print(f"Highest Grades: {high}")
        print(f"Lowest Grade: {low}")

    def save_to_file(self, filename="students.text"):
        with open(filename, "a") as file:
            file.write(f"{self.name}: {self.grades}\n")


student1 = Student("Derin")
student1.add_grade(70)
student1.add_grade(50)
student1.add_grade(40)
student1.add_grade(50)
student1.display_report()
student1.save_to_file()

student2 = Student("JIggy")
student2.add_grade(20)
student2.add_grade(40)
student2.add_grade(50)
student2.add_grade(45)
student2.display_report()
student2.save_to_file()

if student1.cal_average() > student2.cal_average():
    print(f"\n {student1.name} has a higher average than {student2.name}.")
elif student1.cal_average() < student2.cal_average():
    print(f"\n {student2.name} has a higher average than {student1.name}.")
else:
    print(f"\n {student1.name} and {student2.name} have the same average")