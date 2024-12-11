cities = list()  #  list cities = new list(); 
cities.append("Durham")
cities.append("Alice Springs")
cities.append("Reno")
print(f"{type(cities) = }")

class Animal:
    def register(self):
        print("registering...")

class Dog(Animal):
    def bark(self):
        print("woof! woof!")

class Cat(Animal):
    def meow(self):
        print("meow meow meow")

d = Dog()
d.register()
d.bark()

c = Cat()
c.register()
c.meow()