# Reduce(function, iterable, initializer(optional))
"""
Is used to apply a function cumulatively to all elements in an iterable, reducing them to a single value.
It's part of the functools module.
"""

from functools import reduce

def add(x,y):
  print(x,y)
  return x + y

numbers = [1,2,3,4,5]

print(reduce(add, numbers))

# Note: reduce() is useful for complex reductions but should be avoided if built-in functions exist.

print(sum(numbers))