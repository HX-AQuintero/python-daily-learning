# Docstrings
def test(a=None):
  """
  Info: this function tests and prints param a
  """
  print(a)

test('!!!!')
test()

# Getting info using help built-in function
help(test)
help(len)

# Getting info using __doc__ method
print(test.__doc__)
print(len.__doc__)