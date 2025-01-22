# Formatted strings

name = 'Alejo'
age = 28

print('hi ' + name + '. You are ' + str(age) + ' years old')

# Using f (recommended)
print(f'hi {name}. You are {age} years old')

# Dot format
print('hi {}. You are {} years old'.format(name, age))
print('hi {0}. You are {1} years old'.format(name, age))

# Dot format with default values
print('hi {new_name}. You are {new_age} years old'.format(new_name='John', new_age=34))