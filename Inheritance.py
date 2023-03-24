class Animal:
    alive = True

    def eat(self):
        print("It is eating.")

    def sleep(self):
        print("It is sleeping")

class Fish(Animal):
    pass

fish = Fish()
fish.eat()