# Polymorphism
"""
Polymorphism in OOP allows different classes to define methods with the same name but different implementations.
This enables flexibility and code reusability, as different objects can be used interchangeably if they share the
same method names.
"""

class Animal:
  def speak(self):
    return 'Some sound'
  
class Dog(Animal):
  def speak(self):
    return 'Woof!'
  
class Cat(Animal):
  def speak(self):
    return 'Meow!'
  
# Using polymorphism
dog1 = Dog()
cat1 = Cat()
animal1 = Animal()

animals = [dog1, cat1, animal1]

for animal in animals:
  print(animal.speak()) # Woof! Meow! Some sound

# Why does this happen?
# The speak() method behaves differently depending on the object.
# This is method overriding, a key form of polymorphism in inheritance.