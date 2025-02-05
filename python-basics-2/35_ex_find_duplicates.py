some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = []
occurrences = {}

for element in some_list:
  if element not in occurrences:
    occurrences[element] = 1
  else:
    occurrences[element] += 1

for key in occurrences:
  if occurrences[key] >= 2:
    duplicates.append({key: occurrences[key]})

print(duplicates)

# Another solution
duplicates = []
for value in some_list:
  if some_list.count(value) > 1:
    if value not in duplicates:
      duplicates.append(value)

print(duplicates)