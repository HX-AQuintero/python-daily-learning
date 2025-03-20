# Iterables
"""
Are objects or collections that can be iterated over (lists, dictionaries, tuples, sets, strings).
"""

user = {
  'name': 'Golem',
  'age': 5006,
  'can_swim': False
}

for key, value in user.items():
  print(key, value)

for value in user.values():
  print(value)

for keys in user.keys():
  print(keys)

for item in 50:
  print(item) # TypeError: 'int' object is not iterable