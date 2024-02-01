# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("The animal speaks.")


# Child class inheriting from Animal
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        print("The dog barks.")


# Creating objects
animal = Animal("Generic Animal")
dog = Dog("Buddy", "Labrador")

# Calling methods
animal.speak()  # Output: The animal speaks.
dog.speak()  # Output: The dog barks.
