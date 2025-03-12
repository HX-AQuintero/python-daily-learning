# Zip(iterable1, iterable2, ...)
"""
Combines multiple iterables (like lists, tuples, sets, or dictionaries)
element by element, creating pairs (or tuples) from corresponding elements.
"""

my_list = [1,2,3]
your_list = [10, 20, 30]
new_list = (15,25,35)

print(list(zip(my_list, your_list)))
print(list(zip(my_list, new_list)))
print(list(zip(my_list, your_list, new_list)))

# what happens if iterables have different lengths?
names = ['Alice', 'Bob', 'Charlie']
scores = {85, 90}

print(list(zip(names, scores))) # The extra element ('Charlie') is ignored because zip()
                                # stops at the shortest iterable

# zip() with for loops
students = ['Alice', 'Bob', 'Charlie', 'Daniel']
scores = (85, 90, 67, 25)

for student, score in zip(students, scores):
  print(f'{student} scored {score}')