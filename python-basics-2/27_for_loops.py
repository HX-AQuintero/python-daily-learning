# For Loops
"""
Are used to iterate over a sequence (such as a list, tuple, string, dictionary, or range)
and execute a block of code multiple times.
"""

for item in 'Hello World!':
  print(item)

for item in (1,2,3,4,5):
  print(item*2)

for item in [1,2,3,4,5]:
  print(item**3)

for item in {2,4,6,8,10}:
  print(item % 5)

for items in {'a': 1, 'b': 2, 'c': 3}:
  print(items)

# Nested for loops
for item in (1,2,3,4,5):
  for x in ['a', 'b', 'c']:
    print(item, x)

print(item)
print(x)