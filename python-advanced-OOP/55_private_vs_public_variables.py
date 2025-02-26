# Private vs Public Variables

"""
Python does not have truly private variables or methods like some other languages (e.g., Java, C++).
However, single underscore (_var) and double underscore (__var) are conventions used to control access levels.
In Python, public variables can be accessed and modified freely, while private variables (using __var naming convention)
are intended to be hidden from direct access and should only be modified through methods.
"""

class Car:
  def __init__(self, brand, model, speed):
    self.brand = brand # Public attribute (accessible anywhere)
    self.model = model # Public attribute
    self.__speed = speed # Private attribute (should not be accessed directly)

  def accelerate(self, amount):
    """Method to safely modify speed."""
    self.__speed += amount

  def get_speed(self):
    """Getter method to access private variable."""
    return self.__speed

# Creating an instance
car = Car('Toyota', 'Corolla', 50)

# Accessing public attributes directly
print(car.brand) # Toyota
print(car.model) # Corolla

# Accessing private attributes directly
#print(car.__speed) # AttributeError: 'Car' object has no attribute '__speed'. Did you mean: 'get_speed'?

# Accessing private attribute via getter
print(car.get_speed()) # 50

# Modifying speed using method
car.accelerate(20)
print(car.get_speed()) # 70

# What about private methods? 🤔
# It works the same way

class Car:
  def __init__(self, brand, speed):
    self.brand = brand
    self.__speed = speed # Private attribute
  
  def __show_speed(self):
    """Private method (cannot be accessed directly)."""
    return f'{self.brand} is running at {self.__speed} km/h.'
  
car = Car('Ford', 120)

print(car.__speed) # AttributeError: 'Car' object has no attribute '__speed'
print(car.__show_speed()) # AttributeError: 'Car' object has no attribute '__show_speed'. Did you mean: '_Car__show_speed'?

# However,
print(car._Car__speed) # 120
print(car._Car__show_speed()) # Ford is running at 120 km/h.

# What? 🤯🤯🤯
# Direct access to __speed fails, but Python internally renames it to _ClassName__speed, allowing access via "name mangling".


# When to Use Which? 🤔
# - Use _single_underscore ("protected") if you want to signal that an attribute/method is internal but still allow external access if needed.
# - Use __double_underscore ("private") if you want stronger encapsulation and to avoid accidental modifications or overrides in subclasses.