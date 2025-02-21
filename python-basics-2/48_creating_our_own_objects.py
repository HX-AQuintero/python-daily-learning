# Creating our own objects

class PlayerCharacter:
  def __init__(self, name, age):
    self.name = name  # Attributes
    self.age = age

  def run(self):  # Methods
    print('run')

#player0 = PlayerCharacter() 
#print(player0) # TypeError: PlayerCharacter.__init__() missing 1 required positional argument: 'name'

player1 = PlayerCharacter('Alejo', 28)
print(player1) # <__main__.PlayerCharacter object at 0x000001C609036A50>
print(player1.name) # Alejo
print(player1.age) # 28
print(player1.run()) # run

player2 = PlayerCharacter('Tom', 35)
print(player2) # <__main__.PlayerCharacter object at 0x000002D1CE3D8A50>
print(player2.name) # Tom
print(player2.age) # 35
print(player2.run()) # run

print('Is player1 equal to player2?:', player1==player2)