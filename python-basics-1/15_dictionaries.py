# Dictionary
dictionary = {
  'a': 1,
  'b': 2
}

print(dictionary['a'])
print(dictionary['b'])
# print(dictionary['c']) KeyError!

# Dictionaries are actually ordered! 🤯
contestants = { 'Randy Orton': 'Red', 'Dwayne Johnson' : 'Blue' }
contestants['Jhon Cena'] = 'Red'
contestants['Dave Bautista'] = 'Blue'
del contestants['Dwayne Johnson']

print(contestants) 