# Arguments (*args) and Keyword Arguments (**kwargs)

# *args: Accepts any number of positional arguments as a tuple.
# **kwargs: Accepts any number of keyword arguments as a dictionary.

def super_func(*args, **kwargs):
  print(args) # (1, 2, 3, 4, 5)
  print(kwargs) # {'num1': 5, 'num2': 10, 'num3': 4}
  total = 0
  for items in kwargs.values():
    total += items
  return sum(args) + total

print(super_func(1,2,3,4,5, num1=5, num2=10, num3=4)) # 34

# ⚠️ Rule: params, *args, default parameters, **kwargs
def super_complete_func(name, *args, greet='hi', **kwargs):
  return (f"{greet.capitalize()} {name}!\nThe total price adds up to: {sum(args)}\nYou've paid: {sum(kwargs.values())}")

print(super_complete_func('Alejo', 1,2,3,4,5, payment1=2, payment2=4, payment3=6))