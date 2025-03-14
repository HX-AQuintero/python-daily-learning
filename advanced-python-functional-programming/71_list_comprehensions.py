# List Comprehensions
"""
Is a concise way to create lists. It allows to generate a new list by applying an
expression to each item in an itereable, all in a single line of code.
"""

my_list = [char for char in 'hello']
print(my_list)

my_list2 = [num for num in range(0,100)]
print(my_list2)

my_list3 = [num*2 for num in range(0,100)]
print(my_list3)

my_list4 = [num**2 for num in range(0,100) if num % 2 == 0]
print(my_list4)

# Using list comprehension with functions
def double(x):
  return x*2

doubled = [double(num) for num in range(1,6)]
print(doubled)

# Using nested list comprehension
matrix = [[1,2,3],[4,5,6]]
flattened = [num for row in matrix for num in row]
print(flattened)

# Using if-else in list comprehensions
numbers = [num for num in range(1,6)]
result = [num*2 if num % 2 == 0 else num*3 for num in numbers]
print(result)