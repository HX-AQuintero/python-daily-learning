# Enumerate
"""
Adds a counter to an iterable and returns it as an iterator of (index, value) pairs.
"""
for i, char in enumerate('Helloooo'):
  print(i, char)

for i, char in enumerate([1,2,3,4,5]):
  print(i, char)

for i, char in enumerate((1,2,3,4,5)):
  print(i, char)

for i, char in enumerate(list(range(100))):
  if char == 50:
    print(f'index of 50 is: {i}')