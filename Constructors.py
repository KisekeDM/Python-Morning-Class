# Parametarised Constructor
class Employee:
    def __init__(self, firstname, lastname, id):
        self.firstname = firstname
        self.lastname = lastname
        self.id = id

    def info(self):
        print(self.firstname,self.lastname,self.id)

e = Employee("Daniel", "eMobilis", 3)
e.info()
print(getattr(e,"firstname"))
print(hasattr(e,"age"))

# Non-parametarised Constructor
class Student:
    def __init__(self):
        print("No Parameter Available")
    def par(self, name, course, age):
        self.name = name
        self.course = course
        self.age = age
        print(self.name, self.course, self.age)

stu = Student()
stu.display("Daniel", "MIT", 17)
print(getattr(stu,"course"))

