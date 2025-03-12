# Map(function, iterable)
"""
The map function is a built-in function that applies a given function to each item in an iterable
(list, tuple, etc.), returning a new iterable without modifying the original one.
"""
my_list = [1,2,3]
def multiply_by2(item):
  return item*2

my_new_list = list(map(multiply_by2, my_list))
print(my_new_list)
print(my_list)

words = ['hello', 'world', 'my', 'friends']
resulting_words = list(map(str.capitalize, words))
print(resulting_words)
print(words)

# Map with tuples
my_tuple = (1,2,3,4,5,6)
tuple_doubled = tuple(map(multiply_by2, my_tuple))
print(tuple_doubled)
print(my_tuple)

# Map with sets
my_set = {1,2,3,4,5,6,7,8}
set_doubled = set(map(multiply_by2, my_set))
print(set_doubled)
print(my_set)

# Map with dictionaries
data = {1: 'apple', 2: 'banana', 3: 'cherry', 4: 'pear'}

def transform_key_value(item):
  key, value = item
  return (key*2, value.capitalize())

transformed_data = dict(map(transform_key_value, data.items()))
print(transformed_data)
print(data)
print(data.items())