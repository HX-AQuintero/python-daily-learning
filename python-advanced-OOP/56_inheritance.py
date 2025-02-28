# Inheritance
"""
Inheritance is an OOP concept that allows a class (child class) to inherit attributes and methods from
another class (parent class).
This promotes code reuse and enables hierarchical relationships between classes.
"""

class User: # Parent class
  def sign_in(self):
    print('logged in')

class Wizard(User): # Child class
  def __init__(self, name, power):
    self.name = name
    self.power = power
  
  def attack(self):
    print(f'attacking with power of {self.power}')

class Archer(User): # Child class
  def __init__(self, name, num_arrows):
    self.name = name
    self.num_arrows = num_arrows

  def attack(self):
    print(f'attacking with arrows: arrows left-{self.num_arrows}')

wizard1 = Wizard('Merlin', 50) # Instance of Wizard class
archer1 = Archer('Robin', 100) # instance of Archer class

wizard1.attack()
archer1.attack()

wizard1.sign_in() # Inherited method from User
archer1.sign_in() # Inherited method from User

print(isinstance(wizard1, Wizard)) # True 
print(isinstance(wizard1, User)) # True 🤯 why? That's because Wizard class is a subclass of User
print(isinstance(wizard1, object)) # True "Global" parent class