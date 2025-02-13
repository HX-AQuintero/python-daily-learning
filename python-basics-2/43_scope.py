# Scope
"""
What variables do I have access to?
"""

# Global scope
total = 100

if True:
  x = 10

def some_func():
  # Function scope
  total = 200
  print('first print', total)
  print(x)
  
print('second print', total)

some_func()