# Sets

my_set = {1,2,3,4,5}
print(my_set)
# print(my_set[2]) TypeError: 'set' object is not subscriptable

my_set.add(100)
my_set.add(5)
print(my_set)

# Using set() build-in function
my_list = [1,2,3,4,5,5]

print(set(my_list))

new_set = my_set.copy()
print(new_set)