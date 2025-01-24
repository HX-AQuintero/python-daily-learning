# Truthy vs Falsey

""" 
We use "truthy" and "falsy" to differentiate from the bool values True and False.
A "truthy" value will satisfy the check performed by if or while statements.
All values are considered "truthy" except for the following, which are "falsy":

None
False
- Numbers that are numerically equal to zero, including:
    0
    0.0
    0j
    decimal.Decimal(0)
    fraction.Fraction(0, 1)

- Empty sequences and collections, including:
    [] - an empty list
    {} - an empty dict
    () - an empty tuple
    set() - an empty set
    '' - an empty str
    b'' - an empty bytes
    bytearray(b'') - an empty bytearray
    memoryview(b'') - an empty memoryview
    an empty range, like range(0)

- objects for which:
    obj.__bool__() returns False
    obj.__len__() returns 0, given that obj.__bool__ is undefined
"""

is_old = 'hello'
is_licensed = 5

if is_old and is_licensed:
  print('you are old enough to drive, and you have a license!')
else:
  print('you are not of age!')
print('okokok')