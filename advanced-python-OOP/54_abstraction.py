# Abstraction
"""
Abstraction in OOP means hiding unnecessary details and only exposing the essential functionalities of an object.
It allows users to interact with an object through simple and clear methods, without worrying about the complex implementation.
"""

class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model
    self.speed = 0 # Default speed
  
  def drive(self):
    """Abstracts the complex logic of driving into a simple method."""
    return f'{self.brand} {self.model} is now driving.'
  
  def stop(self):
    """Abstracts the stopping mechanism."""
    self.speed = 0
    return f'{self.brand} {self.model} has stopped.'
  
# Creating instances (objects)
car1 = Car('Toyota', 'Corolla')
car2 = Car('Ford', 'Mustang')

# Using the abstracted behavior
print(car1.drive()) # Toyota Corolla is now driving.
print(car2.stop()) # Ford Mustang has stopped.

# Why is this Abstraction? 🤔
# - Hides complex details like how driving or stopping actually works.
# - Provides a simple interface (drive() and stop()) for the user.
# - Users don't need to know how the methods work internally-just call them.

"""
Abstraction simplifies interactions by exposing only necessary functionalities!
"""