# Lambda Expressions
"""
A lambda expression (or lambda function) is a small, anonymous function that can have multiple 
arguments but only one expression. It is often used for short, simple functions that do not
require a formal def statement.
"""

from functools import reduce

add_lambda = lambda x,y: x+y
print(add_lambda(4,6))

# Using lambda inside functions
def multiplier(n):
  return lambda x: x*n

double = multiplier(2)
print(double(8))

# Using lambda with map
numbers = [1,2,3,4]
squared = list(map(lambda item: item**2, numbers))
print(squared)

# Using lambda with filter
evens = list(filter(lambda item: item % 2 == 0, numbers))
print(evens)

# Using lambda with reduce
product = reduce(lambda acc, item: acc * item, numbers)
print(product)