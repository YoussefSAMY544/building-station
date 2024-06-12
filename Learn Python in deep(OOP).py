# Define a base class (superclass)
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")

# Define a subclass that inherits from Animal
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

# Create instances (objects) of Dog and Cat
dog = Dog("Buddy")
cat = Cat("Whiskers")

# Demonstrate polymorphism
for animal in [dog, cat]:
    print(animal.speak())
