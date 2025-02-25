#@classmethod and staticmethod

class PlayerCharacter:
  membership = True
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def shout(self):
    print(f'my name is {self.name}')

  @classmethod
  def adding_things(cls, num1, num2):
    return cls('Teddy', num1 + num2)
  
  @staticmethod
  def adding_things2(num1, num2):
    return num1 + num2
  
#player1 = PlayerCharacter('Tom', 20)
#print(player1.__dict__)
#print(player1.adding_things(4,5))

print(PlayerCharacter.adding_things(3,4).__dict__)
print(PlayerCharacter.adding_things2(3,4))

"""
A @classmethod receives the class itself (cls) as the first argument instead of the instance (self).
This means it can modify or access class attributes.
"""

class MyClass:
  class_variable = 'Hello'

  @classmethod
  def show_class_variable(cls):
    return cls.class_variable # Access class-level attributes

print(MyClass.class_variable) # Hello
print(MyClass.show_class_variable()) # Hello

# When to use @classmethod? 🤔
# When the method needs to access or modify class attributes.
# When creating alternative constructors.

# Alternative constructor with @classmethod
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  @classmethod
  def from_string(cls, person_str):
    name, age = person_str.split(',')
    return cls(name, int(age)) # Creates an instance using cls
  
# Creating objects using the alternative constructor
p1 = Person.from_string("Alice,30")
print(p1.name, p1.age) # Alice 30

# Why use @classmethod here? 🤔
# It allows creating objects using alternative data formats (e.g., a string) without needing an instance.

"""
A @staticmethod does not take self or cls as an argument.
It behaves just like a regular function but lives inside a class.
"""

class MathOperations:
  @staticmethod
  def add(a, b):
    return a + b # No access to class attributes
  
print(MathOperations.add(10, 5)) # 15

# When to use @staticmethod? 🤔
# When a method doesn’t need to access instance (self) or class (cls) attributes.
# When you just want to logically group utility functions inside a class.

# Utility Method with @staticmethod
class TemperatureConverter:
  @staticmethod
  def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
  
print(TemperatureConverter.celsius_to_fahrenheit(25)) # 77.0

# Why use @staticmethod here? 🤔
# This function doesn't depend on instance attributes; it just provides a utility related to temperature conversion.

# Key Differences Between @classmethod and @staticmethod 🗝️
"""
Feature                               | @classmethod                         | @staticmethod
--------------------------------------|--------------------------------------|---------------------------------
Takes self ?                          | No ✖️                                | No ✖️
Takes cls ?                           | Yes ✅                               | No ✖️
Can modify class attributes?          | Yes ✅                               | No ✖️
Can modify instance attributes?       | No ✖️                                | No ✖️
When to use?                          | When working with class-level data   | When working with independent helper functions
"""

# When to Use Which? 🧠
"""
Scenario                                                                 | @classmethod                  | @staticmethod
-------------------------------------------------------------------------|-------------------------------|----------
Need to modify class attributes?                                         | Yes ✅                        | No ✖️
Need to create an alternative constructor?                               | Yes ✅                        | No ✖️
Utility function that doesn't depend on class or instance data?          | No ✖️                         | Yes ✅
Need access to cls inside the method?                                    | Yes ✅                        | No ✖️
"""