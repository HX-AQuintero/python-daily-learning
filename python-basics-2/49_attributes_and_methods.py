# Attributes and Methods

class PlayerCharacter:
  # Class Object Attribute (static)
  membership = True
  def __init__(self, name, age):
    if PlayerCharacter.membership:
      self.name = name  # Attributes
      self.age = age

  def shout(self):  # Methods
    print(f'My name is {self.name}, and my membership is {PlayerCharacter.membership}')

player1 = PlayerCharacter('Cindy', 44)
player2 = PlayerCharacter('Tom', 21)
player2.attack = 50

print(player1.shout())
print(player2.shout())

"""
A Class Object Attribute (also called a Class Attribute) is a variable that is shared across all instances of a class.
It is defined directly inside the class, outside any methods, unlike instance attributes which are specific to each object.
"""

# Difference between Class Attributes and Instance Attributes
"""
Feature                   | Class Attribute                         | Instance Attribute
--------------------------|-----------------------------------------|---------------------------------
Defined in                | Inside the class, outside methods       | Inside the __init__ method
Scope                     | Shared by all instances                 | Unique to each instance
Can be modified?          | Yes, but changes affect all instances   | Yes, but only for that instance
"""

class Car:
  wheels = 4 # Class attribute (shared by all instances)

  def __init__(self, brand):
    self.brand = brand # Instance attribute (unique per object)

# Creating instances
car1 = Car('Toyota')
car2 = Car('Ford')

print(car1.brand) # Toyota
print(car2.brand) # Ford

print(car1.wheels) # 4
print(car2.wheels) # 4

# What happens if we modify the class function❓
# The change affects all instances because wheels is a class attribute ✅
Car.wheels = 6
print(car1.wheels) # 6
print(car2.wheels) # 6


# What if we modify wheels only for car1❓
# This does not change the class attribute but creates a new instance attribute in car1
car1.wheels = 8 # Creates a new instance attribute in car1
print(car1.wheels) # 8 (modified only for car1)
print(car2.wheels) # 6 (still follows the class attribute)

# When to Use Class Attributes? 🤔
# For values shared among all instances, like default configurations.
# To count instances of a class, useful in patterns like Singleton.

class Person:
  count = 0  # Class attribute

  def __init__(self, name):
    self.name = name  # Instance attribute
    Person.count += 1  # Increments the shared counter

print(Person.count)  # 0
p1 = Person("Alice")
p2 = Person("Bob")
print(Person.count)  # 2
