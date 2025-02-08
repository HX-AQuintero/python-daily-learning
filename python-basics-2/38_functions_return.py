# Return
""" 
To consider about functions:

- Should do one thing really well.
- Should return something.
"""

def sum(num1, num2):
  return num1 + num2

print(sum(4,5))

total = sum(10,98)
print(total)

total2 = print(sum(8,total))

# Another example
def sum2(num1, num2):
  def another_func(num1, num2):
    return num1 + num2

total = sum2(4,5)
print(total) # None why? 🤯 That's because the return belongs to the inner function

# How to solve this?
def sum2_solved(num1, num2):
  def another_func(num1, num2):
    return num1 + num2
  return another_func(num1, num2)

total = sum2_solved(10,20)
print(total)