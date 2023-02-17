class Student:
    school = 'skill'

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return self.m / 3

    @classmethod
    def info(cls):
        return cls.school

    @staticmethod
    def class_method():
        return "This is a static method"


# s1 = Student(34,67,32)
# s2 = Student(89,56,88)
# print(Student.class_method())

class Employee:
    raise_amt = 1.04

    def __init__(self, first, last, pay, firs=None):
        self.first = first
        self.last = last
        self.email = first + '. ' + last + "@email.com"
        self.pay = pay

    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def __str__(self):
        return "{} - {}".format(self.fullname(), self.email)

    def __repr__(self):
        return "Employee('{}','{}','{}')".format(self.first, self.last, self.pay)

    def __add__(self, other):
        return self.pay + other.pay

    def __mul__(self, other):
        return self.pay * other.pay

    def __len__(self):
        return len(self.fullname())


emp1 = Employee("randy", "orton", 60000)
emp2 = Employee("Jhon", "Cena", 80000)

# print(emp1.first+' '+emp1.last)
# print(emp1.__repr__())
# print(emp1.fullname())
# print(emp1+emp2)
# print(emp2.fullname(),emp1.__len__())
