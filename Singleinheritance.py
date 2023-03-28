class Dog:
    def speak(self):
        print("Barking")

class Puppy(Dog):
    def play(self):
        print("Playing")

d = Dog()
d.speak()

p = Puppy()
p.play()
p.speak()
print(issubclass(Puppy,Dog))
print(isinstance(d,Dog))
print(isinstance(d,Puppy))