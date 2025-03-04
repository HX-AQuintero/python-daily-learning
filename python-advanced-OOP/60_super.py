# Super
"""
super() is used to call methods from a parent class without referring to the parent class explicitly.
This helps with code reusability, method overriding, and multiple inheritance.
"""

class Animal:
  def __init__(self, species, legs):
    self.__species = species # It won't be inherited
    self.legs = legs # It will be inherited

  def move(self): # It will be inherited
    return 'Moves in some way' 
  
  def __sound(self): # It won't be inherited
    return 'Some generic sound'
  
class Bird(Animal):
  def __init__(self, legs, wing_span):
    super().__init__('Bird', legs)
    self.wing_span = wing_span # Custom attribute not in parent class

  def fly(self):
    return 'Flies in the sky'
  
  def move(self):
    return super().move() + ' quickly!'
  
sparrow = Bird(2, "Small")

print(sparrow.legs) # 2
print(sparrow.move()) # Moves in some way quickly!
print(sparrow.wing_span) # Small

#print(sparrow.species) # AttributeError: 'Bird' object has no attribute 'species'
print(sparrow._Animal__species) # Bird (because of name mangling)

#print(sparrow.sound()) # AttributeError: 'Bird' object has no attribute 'sound'
print(sparrow._Animal__sound()) # Some generic sound (because of name mangling)

"""
- super() does not block anything.
- Restrictions must be done in the parent class (e.g., using private attributes __var or overriding methods).
"""