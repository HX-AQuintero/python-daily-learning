# Encapsulation
"""
This means binding of data and functions that manipulate that data.
Encapsulation in OOP means grouping related data (attributes) and
behaviors (methods) inside a class, so that objects (instances) manage
their own state and behavior.
"""

class Car:
  def __init__(self, brand, model, speed):
    self.brand = brand # Attributes(data)
    self.model = model
    self.speed = speed

  def accelerate(self, amount):
    """Method to increase speed."""
    self.speed += amount
  
  def brake(self, amount):
    """Method to decrease speed."""
    self.speed -= amount if self.speed - amount >= 0 else self.speed

  def show_info(self):
    """Method to display car details."""
    return f'{self.brand} {self.model} is running at {self.speed} km/h.'
  
# Creating instances (objects)
car1 = Car('Toyota', 'Corolla', 50)
car2 = Car('Ford', 'Mustang', 70)

# interacting with the objects
car1.accelerate(20)
print(car1.show_info()) # Toyota Corolla is running at 70 km/h.

car2.brake(50)
print(car2.show_info()) # Ford Mustang is running at 20 km/h.

# Why is this Encapsulation? 🤔
# - Data (attributes) and behavior (methods) are inside the class.
# - Objects (car1, car2) manage their own state independently.
# - Methods control how attributes are changed (e.g., accelerate, brake).

"""
Encapsulation ensures that each object is responsible
for its own behavior, keeping the code organized and modular.
"""
