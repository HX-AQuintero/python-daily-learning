# Tuples

my_tuple=(1,2,3,4,5)
# my_tuple[1] = 9 TypeError: 'tuple' object does not support item assignment
print(my_tuple)
print(my_tuple[2])
print(5 in my_tuple)

user = {
  (1,2): [1,2,3],
  'greet': 'hello',
  'age': 20
}

print(user[(1,2)])