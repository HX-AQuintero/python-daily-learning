# Exercise lambda expressions

# Square
my_list = [5,4,3]
print(list(map(lambda item: item**2, my_list)))

# List Sorting
list = [(0,2), (4,3), (9,9), (10, -1)]

def sorter(a):
  for i in range(len(a)):
    for j in range(len(a)-i-1):
      if a[j][1] >= a[j+1][1]:
        a[j], a[j+1] = a[j+1], a[j]
  return a

print(sorter(list))

# A better solution using lambda expressions
list = [(0,2), (4,3), (9,9), (10, -1)]
list.sort(key=lambda x: x[1])
print(list)