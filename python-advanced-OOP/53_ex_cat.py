# Exercise cat
# Given the below class:
class Cat:
  species = 'mammal'
  def __init__(self, name, age):
    self.name = name
    self.age = age

# 1. Instantiate the Cat object with 3 cats
cat1 = Cat('Apolo', 1)
cat2 = Cat('Michi', 4)
cat3 = Cat('Garfield', 2)

#print(cat1.__dict__)
#print(cat2.__dict__)
#print(cat3.__dict__)

# 2. Create a function that finds the oldest cat
def oldest_cat(cats):
  """
  This function receives an array of Cat instances and returns the oldest cat from there
  """
  oldest = cats[0]
  for cat in cats:
    if cat.age >= oldest.age:
      oldest = cat
  return f'The oldest cat is {oldest.age} years old.'

# 3. Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
cats = [cat1, cat2, cat3]
print(oldest_cat(cats))

# Another solution
def oldest_cat1(cats):
   def get_age(cat):
     return cat.age
   return max(cats, key=get_age)

oldest=oldest_cat1(cats)
print(f'The oldest cat is {oldest.age} years old.')

# improved version
# Define the Cat class
class Cat:
  species = 'mammal'
  
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __repr__(self):
    return f"Cat(name='{self.name}', age={self.age})"  # For better debugging

# Instantiate Cat objects
cats = [
    Cat('Apolo', 1),
    Cat('Michi', 4),
    Cat('Garfield', 2)
]

# Function to find the oldest cat
def oldest_cat2(cats):
  return max(cats, key=lambda cat: cat.age)  # Uses max() with a key function

# Find the oldest cat and print the result
oldest2 = oldest_cat2(cats)
print(f"The oldest cat is {oldest2.name}, who is {oldest2.age} years old.")