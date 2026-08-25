"""
Module 5: Object-Oriented Programming (OOP)
============================================
Learn classes, inheritance, and encapsulation in Python.
Copilot tip: describe the class purpose in a docstring and Copilot will suggest attributes and methods.
"""


# ---------- Base class ----------
class Animal:
    """Represents a generic animal."""

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self._hunger = 0       # protected attribute

    def eat(self):
        """Reduce hunger level."""
        self._hunger = max(0, self._hunger - 1)
        return f"{self.name} eats some food."

    def speak(self):
        """Return the animal's sound (to be overridden)."""
        return f"{self.name} makes a sound."

    def __repr__(self):
        return f"Animal(name={self.name!r}, species={self.species!r})"


# ---------- Subclass with inheritance ----------
class Dog(Animal):
    """Represents a dog — a specialisation of Animal."""

    def __init__(self, name, breed):
        super().__init__(name, species="Canis lupus familiaris")
        self.breed = breed

    def speak(self):
        """Dogs bark."""
        return f"{self.name} says: Woof!"

    def fetch(self, item="ball"):
        """Dog fetches an item."""
        return f"{self.name} fetches the {item}!"


# ---------- Another subclass ----------
class Cat(Animal):
    """Represents a cat."""

    def __init__(self, name, indoor=True):
        super().__init__(name, species="Felis catus")
        self.indoor = indoor

    def speak(self):
        return f"{self.name} says: Meow!"


import math


# ---------- Class method & static method ----------
class MathHelper:
    """Utility class demonstrating class/static methods."""

    @classmethod
    def circle_area(cls, radius):
        """Calculate area of a circle using math.pi."""
        return math.pi * radius ** 2

    @staticmethod
    def is_even(n):
        """Return True if n is even."""
        return n % 2 == 0


# ---------- Running examples ----------
if __name__ == "__main__":
    dog = Dog("Rex", "Labrador")
    cat = Cat("Whiskers")

    print(dog.speak())
    print(cat.speak())
    print(dog.fetch("stick"))
    print(dog.eat())

    animals = [dog, cat]
    for animal in animals:
        print(animal)

    print(f"\nCircle area (r=5): {MathHelper.circle_area(5):.2f}")
    print(f"Is 4 even? {MathHelper.is_even(4)}")
    print(f"Is 7 even? {MathHelper.is_even(7)}")
