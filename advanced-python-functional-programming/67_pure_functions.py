# Pure Functions
"""
A pure function is a function that:
- Always returns the same output for the same input (no randomness, no external state changes).
- Has no side effects (does not modify variables, files, or databases outside its scope).
- Does not depend on or modify global state.

Pure functions ensure predictability, testability, and reusability.
"""
# Basic pure function
def add(a,b):
  return a + b # No external changes

print(add(2,3)) # 5
print(add(2,3)) # Always returns 5 (same input -> same output)

# Impure function (with side effects)
total = 0 # External state
def add_to_total(value):
  global total
  total += value # Modifies external state
  return total

print(add_to_total(5)) # Output depends on global state (not pure)
print(add_to_total(5)) # Different output each time (not predictable)

# Impure function (modifying output)
def multiply_in_place(numbers):
  for i in range(len(numbers)):
    numbers[i] *= 2 # Modifies the input list

nums = [1,2,3]
multiply_in_place(nums)
print(nums) # Original list is changed [2,4,6]

# Pure function
def multiply_by2(li):
  new_list = []
  for item in li:
    new_list.append(item*2)
  return new_list

print(multiply_by2([1,2,3]))