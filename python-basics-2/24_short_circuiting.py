#Short Circuiting

# First case
is_Friend = True
is_User = True

if is_Friend or is_User:
  print('best friends forever') # It's enough checking the first value because of the "or" to print this out
                                # Short-circuit ⚡🔌

if is_Friend and is_User:
  print('best friends forever') # It must check both values because of the "and" to print this out

# Second case
is_Friend = False
is_User = True

if is_Friend or is_User:
  print('best friends forever') # It must check the second value because of the "or" to print this out

if is_Friend and is_User:
  print('best friends forever') # It's enough checking the first value because of the "and" to don't print this out
                                # Short-circuit ⚡🔌