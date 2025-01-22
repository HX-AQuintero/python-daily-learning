# Dictionary methods
user = {
  'basket': [1,2,3],
  'greet': 'hello',
  #'age': 20
}

# print(user['age']) KeyError: 'age'

# Avoiding key errors
print(user.get('age')) # None (by default)
print(user.get('age', 55)) # 55

# A new way to create a dictionary (not very common)
user2 = dict(name='Vicky')
print(user2)