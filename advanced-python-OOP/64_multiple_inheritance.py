# Multiple Inheritance
"""
Allows a class to inherit from more than one parent class.
This means a child class can access attributes and methods from multiple sources.
"""

class User:
  def sign_in(self):
    print('logged in')

class Wizard(User):
  def __init__(self, name, power):
    self.name = name
    self.power = power

  def attack(self):
    print(f'attacking with power of {self.power}')

class Archer(User):
  def __init__(self, name, arrows):
    self.name = name
    self.arrows = arrows

  def check_arrows(self):
    print(f'{self.arrows} remaining')

  def run(self):
    print('ran really fast')

class HybridBorg(Wizard, Archer):
  pass

hybridborg1 = HybridBorg('borgie', 50)
#print(hybridborg1.run())
#print(hybridborg1.check_arrows()) # AttributeError: 'HybridBorg' object has no attribute 'arrows'

# How could we fix this? 🤔
class HybridBorg(Wizard, Archer):
  def __init__(self, name, power, arrows):
    Archer.__init__(self, name, arrows)
    Wizard.__init__(self, name, power)
    #super().__init__(self, name, power, arrows) # Doesn't work

hybridborg2 = HybridBorg('borgie2', 50, 100)
print(hybridborg2.check_arrows())
print(hybridborg2.attack())
print(hybridborg2.sign_in())