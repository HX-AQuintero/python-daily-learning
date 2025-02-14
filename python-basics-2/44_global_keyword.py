# Global keyword

total = 0

def count():
  total += 1
  return total

print(count()) # UnboundLocalError: cannot access local variable 'total' where it is not associated with a value

# How to fix this? 🛠️
"""
We need to explicitly tell that total is a global variable to get access to it.
The global total statement tells Python to use the total variable from the global
scope instead of creating a new local variable.
"""
def count():
  global total
  total += 1
  return total

print(count())
print(count())
print(count())

# However, this is a bad code practices👎
# This could lead to side effects on the outside global scope

# A better solution using dependency injection 🧠
"""
Instead of modifying a global variable directly, a better practice is to pass total
as a parameter and return the updated value.
"""
def count(total):
  total += 1
  return total

print(count(count(count(total))))

"""
- This avoids modifying global state inside a function (which is generally considered bad practice).
- The function works independently without needing global variables.
- It makes debugging and testing easier.
"""