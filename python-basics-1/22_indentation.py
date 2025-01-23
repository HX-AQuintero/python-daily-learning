# Indentation
""" 
The interpreter actually finds meaning in the spaces.
That's the selling part in Python
"""

is_old = True
is_licensed = False

#Case 1
if is_old and is_licensed:
  print('you are old enough to drive, and you have a license!')
else:
  print('you are not of age!')
  print('okokok') # It will also be printed when else is satisfied

#Case 2
if is_old and is_licensed:
  print('you are old enough to drive, and you have a license!')
else:
  print('you are not of age!')
print('okokok') # It won't be printed when else is satisfied