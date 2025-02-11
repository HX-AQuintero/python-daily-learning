# Clean Code

def is_even(num):
  if num % 2 == 0:
    return True
  else:
    return False

print(is_even(50))
print(is_even(51))

# How can we improve the code? make it shorter?
def is_even2(num):
  return True if num % 2 == 0 else False

print(is_even2(50))
print(is_even2(51))

# Even better
def is_even3(num):
  return num % 2 == 0

print(is_even3(50))
print(is_even3(51))