# Filter(function, iterable)
"""
The filter function is a built-in function that is used to filiter elements from an iterabole based on a condition.
It applies a function that returns True or False to each element and keeps only those that return True.
"""

numbers = [1,2,3,4,5,6]
def is_even(number):
  return number % 2 == 0

filtered_numbers = list(filter(is_even, numbers))
print(filtered_numbers)
print(numbers)

names = ("Alice", "Bob", "Anna", "Charlie", "Alex")
def starts_with_a(name):
  return name[0].upper() == "A"

filtered_names = tuple(filter(starts_with_a, names))
print(filtered_names)
print(names)

# Filter with sets
words = {"hello", " ", "", "world", "  ", "Python"}
def is_not_empty(text):
  return bool(text.strip())

filtered_words = set(filter(is_not_empty, words))
print(filtered_words)
print(words)

# Filter with dictionaries
grades = {"Alice": 45, "Bob": 78, "Charlie": 92, "David": 30}
def is_above_50(item):
  key, value = item
  return value > 50

filtered_grades = dict(filter(is_above_50, grades.items()))

print(filtered_grades)
print(grades)