# Conditional logic
is_old = True
is_licensed = True

# One way
if is_old:
  print('you are old enough to drive!')
elif is_licensed:
  print('you can drive now!')
else:
  print('you are not of age!')
print('okokok')

# Using two conditions to satisfy
if is_old and is_licensed:
  print('you are old enough to drive, and you have a license!')
else:
  print('you are not of age!')
print('okokok')