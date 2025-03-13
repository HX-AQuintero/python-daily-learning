# Exercise lambda expressions

# Square
my_list = [5,4,3]
print(list(map(lambda item: item**2, my_list)))

# List Sorting
a = [(0,2), (4,3), (9,9), (10, -1)]

def sorter(a):
  b = []
  for i in range(len(a)):
    for j in range(len(a)-1):
      initial_value = a[0]
      if a[i][1] <= a[j+1][1]:
        a[i] = a[j+1]
        initial_value = a[i]
      b.append(initial_value)
  return b

print(sorter(a))