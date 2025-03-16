# Logical Operators
"""
Are used to combine boolean expressions (conditions that evaluate to True or False).
These operators return True or False based on the logic they implement.

and -> Returns True if both conditions are True
or -> Returns True if at least one condition is True
not -> Reverses the boolean value
"""

# And
x = 5
y = 10

if x > 0 and y > 5:
  print("Both conditions are True")  # ✅ This will execute
else:
  print("At least one condition is False")

# Or
x = 5
y = -10

if x > 0 or y > 0:
  print("At least one condition is True")  # ✅ This will execute
else:
  print("Both conditions are False")

# Not
x = False

if not x:
  print("x is False, so this runs")  # ✅ This will execute
