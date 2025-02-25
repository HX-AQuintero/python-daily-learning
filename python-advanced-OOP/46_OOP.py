# OOP I
"""
Everything in Python is an object and is built by the class keyword.
"""
print(type(None)) # <class 'NoneType'>
print(type(True)) # <class 'bool'>
print(type(5)) # <class 'int'>
print(type(5.5)) # <class 'float'>
print(type('hi')) # <class 'str'>
print(type([])) # <class 'list'>
print(type(())) # <class 'tuple'>
print(type({})) # <class 'dict'>

"""
But, what's an object?
An object is an instance of a class.
Has attributes (data) and methods (functions) to operate with.
"""
class Car:
  def __init__(self, brand):
    self.brand = brand  # Attribute

  def drive(self):  # Method
    return f"You are driving a {self.brand}"

# Creating an object (instance) of the Car class
my_car = Car("Toyota")

print(my_car.brand)  # Accessing attribute -> Toyota
print(my_car.drive())  # Calling method -> You are driving a Toyota
