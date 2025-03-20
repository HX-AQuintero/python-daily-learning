# Decorators
"""
Is a function that modifies the behavior of another function or method without changing its code.
Decorators allow us to wrap functions dynamically, adding extra functionality before or after
the original function runs.
"""

def decorator_function(original_function):
  def wrapper_function():
    print('*************')
    original_function()  # Call the original function
    print('*************')
  return wrapper_function

@decorator_function  # ✅ Applying the decorator
def greet():
  print('Hello, world!')

@decorator_function  # ✅ Applying the decorator
def bye():
  print('see ya later!')

greet()
bye()

# How does this work under the hood? 🤔
def decorator_function(original_function):
  def wrapper_function():
    print('*************')
    original_function()  # Call the original function
    print('*************')
  return wrapper_function

def greet():
  print('Hello, world!')

def bye():
  print('see ya later!')

greet2 = decorator_function(greet)
greet2()

bye2 = decorator_function(bye)
bye2()