my_set = {1,2,3,4,5}
your_set = {4,5,6,7,8,9,10}

# Difference
print(my_set.difference(your_set))
print(your_set.difference(my_set))

# Discard
""" print(my_set.discard(5))
print(my_set.discard(56))
print(my_set) """

# Difference update
""" print(my_set.difference_update(your_set))
print(my_set) """

# Intersection
print(my_set.intersection(your_set))
print(my_set & your_set)

# Is disjoint
print(my_set.isdisjoint(your_set))

# Is subset
print(my_set.issubset(your_set))

# Is superset
print(my_set.issuperset(your_set))

# Union
print(my_set.union(your_set))
print(my_set | your_set)