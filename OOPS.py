class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name :", self.name)
        print("Age :", self.age)


class Student(Person):
    def __init__(self, rollno, name, age, per):
        self.rollno = rollno
        Person.__init__(self, name, age)
        self.per = per

    def display(self):
        print("Rollno :", self.rollno)
        Person.display(self)
        print("Percentage : ", self.per)


s1 = Student(101, "Hema", 21, 75.50)
print("Student Details : ")
# s1.display()
# print(s1.rollno)
print(s1.display())
