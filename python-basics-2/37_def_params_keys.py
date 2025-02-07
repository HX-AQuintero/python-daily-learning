def say_hello(name, emoji):
  print(f'helloooo, {name} {emoji}')

# Keyword arguments
""" 
I tell explicitly what arguments I'm giving to the function parameters instead of the positional arguments (previous topic).

This is actually a bad practice 👎 make the code more complicated that it needs to be.
"""
say_hello(emoji=':(', name='Vicky')

# Default parameters
""" 
Allow us to give right as we're defining a functino what we wnat as default.
"""
def say_hello2(name='Darth Vader', emoji='>:v'):
  print(f'helloooo, {name} {emoji}')

say_hello2() # It works because of the default parameters
say_hello2('Alejo')
say_hello2(emoji=':D') # I need to pass explicitly using keyword arguments
