class Student:
    college_name = "Lovely Professional University"
    # default constructor
    def __init__():
        pass

    # paramterized constructor
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
        print("Abhinav Kumar Jha")

s1 = Student("Dipanshu",200)
print(s1.name,s1.marks)
s2 = Student("Saptak",200)
print(s2.name,s2.marks)
print(Student.college_name)
print(s1.college_name)