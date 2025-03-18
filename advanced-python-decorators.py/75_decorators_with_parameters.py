# Decorator Pattern

def decorator_function(original_function):
  def wrapper_function(*args, **kwargs):
    original_function(*args, **kwargs)  # Call the original function
  return wrapper_function

@decorator_function  # ✅ Applying the decorator
def greet(greeting, emoji=':('):
  print(greeting, emoji)

greet('hiiiii')