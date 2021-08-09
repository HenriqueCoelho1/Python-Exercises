# no orinted programming object
# student = {"name": "Rafael", "grades": (80, 88, 99, 69, 60)}


# def average(sequence):
#     return sum(sequence) / len(sequence)


# print(average(student["grades"]))

class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average(self):
        return sum(self.grades) / len(self.grades)


student = Student("Nick", (90, 88, 99, 69, 90))
student2 = Student("Rolf", (70, 88, 29, 79, 76))
print(student.name)
print(student.grades)
print(student.average())  # || print(Student.average(student))
print(student2.average())
