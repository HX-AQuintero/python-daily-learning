# Nonlocal keyword

"""
The nonlocal keyword in Python is used inside nested functions to indicate that
a variable refers to a variable in the nearest enclosing scope (excluding the global scope).
It allows modifying the value of a non-global variable from an inner function.
"""

def outer():
  x = 'local'
  def inner():
    nonlocal x
    x = 'nonlocal'
    print('inner:', x) # inner: nonlocal

  inner()
  print('outer:', x) # outer: nonlocal

outer()

# Without nonlocal, the inner function would create a new local variable instead of modifying the outer variable.