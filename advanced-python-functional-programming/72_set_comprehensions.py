# Set Comprehensions
"""
 Is a concise way to create sets and dictionaries, similar to list comprehensions.
 It allows you to generate a set or dictionary by applying an expression to each
 element in an iterable, all in a single line of code.
"""

my_set = {char for char in 'hello'}
print(my_set)

my_set2 = {num for num in range(0,100)}
print(my_set2)

my_set3 = {num*2 for num in range(0,100)}
print(my_set3)

my_set4 = {num**2 for num in range(0,100) if num % 2 == 0}
print(my_set4)

# Using set comprehension with functions
def double(x):
  return x*2

doubled = {double(num) for num in range(1,6)}
print(doubled)

# Using if-else in set comprehensions
numbers = {num for num in range(1,6)}
result = {num*2 if num % 2 == 0 else num*3 for num in numbers}
print(result)

# Dictionary Comprehensions
simple_dict = {
  'a': 1,
  'b': 2
}

my_dict = {k:v**2 for k,v in simple_dict.items() if v%2==0}
print(my_dict)

my_dict2 = {num:num*2 for num in [1,2,3]}
print(my_dict2)