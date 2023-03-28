class Animal:
    def speak(self):
        print("speaking")

class Dog(Animal):
    def speak(self):
        print("Barking")

class Bee(Dog):
    def speak(self):
        print("Buzzing")

b = Bee
b.speak()