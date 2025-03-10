# Exercise pet
class Pets:
  animals = []
  def __init__(self, animals):
    self.animals = animals

  def walk(self):
    for animal in self.animals:
      print(animal.walk())

class Cat():
  is_lazy = True

  def __init__(self, name, age):
    self.name = name
    self.age = age
  
  def walk(self):
    return f'{self.name} is just walking around'
  
class Apollo(Cat):
  def sing(self, sounds):
    return f'{sounds}'
  
class Sally(Cat):
  def sing(self, sounds):
    return f'{sounds}'
  
# 1. Add another Cat
class Michi(Cat):
  def sing(self, sounds):
    return f'{sounds}'

# 2. Create a list of all of the pets (create 3 cat instances from the above)
my_cats = []
apollo1 = Apollo('Apollo', 1)
sally1 = Sally('Sally', 2)
michi1 = Michi('Michi', 3)

my_cats.append(apollo1)
my_cats.append(sally1)
my_cats.append(michi1)

# 3. Instantiate the Pet class with all your cats use variable my_pets
my_pets = Pets(my_cats)
#help(my_pets) # Print all attributes and methods
#print(dir(my_pets)) # Print all attributes and methods
#print(my_pets.__dict__) # Print all the attributes

# 4. Output all of the cats walking using the my_pets instance
my_pets.walk()