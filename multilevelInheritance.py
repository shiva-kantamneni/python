# Base class
class Animal:
    def speak(self):
        print("Animals can make sounds.")

# Derived from Animal
class Mammal(Animal):
    def feature(self):
        print("Mammals give birth to young ones.")

# Derived from Mammal
class Dog(Mammal):
    def breed(self):
        print("Dogs are loyal animals.")

# Creating object of Dog
dog = Dog()

# Accessing methods from all classes
dog.speak()     # From Animal
dog.feature()   # From Mammal
dog.breed()     # From Dog
