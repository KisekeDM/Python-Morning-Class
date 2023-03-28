class Employee:
    def eat(self):
        print("eating")

class Manager(Employee):
    def task(self):
        print("Coordinating")

class Cook(Manager):
    def role(self):
        print("cooking")

m = Manager()
m.task()

c = Cook()
c.role()

print(isinstance(m,Manager))
print(issubclass(Cook,Employee))
