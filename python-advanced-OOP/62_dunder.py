# Dunder methods
"""
(Short for double underscore methods) are special methods in Python that begin and end with double
undercores (__method__).
They enable objects to work with built-in operations like addition (+), length (len()), iteration,
string representation, and more.
"""

class Toy:
  def __init__(self, color, age):
    self.color = color
    self.age = age
    self.my_dict = {
      'name': 'Ale',
      'has_pets': False
    }

  def __str__(self):
    return f'The toy is {self.color}'
  
  def __len__(self):
    return 5
  
  def __del__(self):
    print('deleted')
  
  def __call__(self, name):
    return f'yes??, {name}'
  
  def __getitem__(self, i):
    return self.my_dict[i]

action_figure1 = Toy('red', 0)

print(action_figure1.__str__())
print(str(action_figure1))

print(action_figure1.__len__())
print(len(action_figure1))

#del(action_figure1)
#print(len(action_figure1)) # NameError: name 'action_figure1' is not defined

print(action_figure1.__call__('Ale'))

print(action_figure1['name'])

# How does this work? 🤔
"""
- If there is a __str__ dunder method, str() calls it, if not, calls __repr__.
If this latter is missing, the result will be a not user-friendly output. It's
a good practices to define one of them.
- If there is a __len__ dunder method, len() calls it, if not, raise an error
(TypeError: object of type 'Toy' has no len())
- __call__ makes the object callable.
- Python automatically calls __del__ when an object has no more references, meaning
nothing in the program is using it.
- The __getitem__() method allows objects to support indexing like lists.
"""