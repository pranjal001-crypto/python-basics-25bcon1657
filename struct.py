from dataclasses import dataclass

@dataclass
class Student:
    name: str
    roll_no: int
    marks: float

def display(student):
    print("Student Name:", student.name)
    print("Roll Number:", student.roll_no)
    print("Marks:", student.marks)

s = Student("Rahul", 101, 87.5)

display(s)
