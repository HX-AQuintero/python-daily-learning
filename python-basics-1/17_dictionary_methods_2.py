# Dictionary methods 2
user = {
  'basket': [1,2,3],
  'greet': 'hello',
  'age': 20
}

print('basket' in user)
print('size' in user)
print('hello' in user)

# .keys()
print(user.keys())
print('basket' in user.keys())
print('size' in user.keys())

# .values()
print(user.values())
print('hello' in user.values())

# .items()
print(user.items())

# .clear()
#user.clear()
#print(user)

# .copy()
user2 = user.copy()
print(user==user2)

user['size'] = 200
print(user)
print(user2)

# .pop()
print(user.pop('size'))
print(user.pop('nickname', 'key doesn\'t exist'))
# print(user.pop('nickname')) KeyError!

# .popitem()
#user.popitem()

# .update()
user.update({'age': 23})
# user.update({'ages': 23}) if the key doesn't exist, it's going to add it with its value
print(user)