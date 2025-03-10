# __init__

"""
The __init__ method in Python is a special method (or constructor) used to initialize new objects
when they are created. It sets up initial attributes and ensures that an object starts with valid data.
"""

class PlayerCharacter:
  def __init__(self, name='anonymous', age=0): # Using default values
    #if age > 18:
      self.name = name
      self.age = age

  def shout(self):
    return(f'my name is {self.name}, and I\'m {self.age} years old')

player1 = PlayerCharacter('Tom', 10)
player2 = PlayerCharacter()

print(player1.shout()) # my name is Tom, and I'm 10 years old
print(player2.shout()) # my name is anonymous, and I'm 0 years old

# Why is __init__ important? 🤔
# Ensures objects start with valid data.
# Eliminates the need for manual attribute assignments after object creation.
# Allows flexibility when creating multiple objects with different values.

# Defining a class without __init__ method
class Person:
  pass # No __init__

p1 = Person()
p1.name = 'Tom'
p1.age = 10

# This is less efficient and more error-prone than defining attributes inside __init__ ✖️

# Can __init__ return a value? 🤔
# No, __init__ method cannot return anything other than None.
# Unlike normal methods, __init__ is only meant for object initialization, not for returning values.

class Test:
   def __init__(self):
      return "Hello"

test1 = Test()
print(test1) # TypeError: __init__() should return None, not 'str'

# Python doesn't run __init__ until you create an instance of the class.
class Example:
   def __init__(self):
      print("Object created!")

print("Class defined!")  # This runs first

e = Example()  # This triggers __init__
