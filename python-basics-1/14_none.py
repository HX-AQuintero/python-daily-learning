# None

"""
Represents the absence of value.
In other languages, it's named Null.

Why is this useful?
Defining a variable as None is useful because:
"""

# It acts as a placeholder.
result = None  # Placeholder before assigning an actual value

# It allows optional function arguments.
def greet(name=None):
  if name is None:
    print("Hello, guest!")
  else:
    print(f"Hello, {name}!")

greet()      # Output: Hello, guest!
greet("Sam") # Output: Hello, Sam!

# It signals the absence of a value.
data = [1, 2, 3]
data = None  # Now data is explicitly empty

def do_nothing():
  pass

print(do_nothing())  # Output: None


# It prevents accidental use of undeclared variables.
config = None

if config is None:
  print("No configuration found. Using defaults.")

# It improves readability and maintainability.
user_status = None  # Means "no status available"
user_status = ""    # Could mean "empty status" instead of "no status"