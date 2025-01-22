# List slicing
""" new_list = ['a', 'b', 'c']
print(new_list[1])
print(new_list[-2])
print(new_list[1:3])
new_list[0] = 'z'
print(new_list)

my_list = [1,2,3]
bonus = my_list + [5]
my_list[0] = 'z'
print(my_list)
print(bonus) """

shopping_cart = [
  'notebooks',
  'sunglasses',
  'toys',
  'grapes'
]

""" print(shopping_cart[0])
print(shopping_cart[0:2])
print(shopping_cart[0::2]) """

# Lists are mutable
""" shopping_cart[0] = 'laptop'
new_cart = shopping_cart[0:3]
new_cart[0] = 'gum'
print(new_cart)
print(shopping_cart) """

# Let's give it a shot
new_cart = shopping_cart
print('first print: ', new_cart)
new_cart[0] = 'gum'
print('second print: ', new_cart)
print('third print: ', shopping_cart) # It's modified! 🤯 why? hey, now new_cart is equal to whatever's in the memory of shopping_cart

# To avoid the previous situation and create a copy
new_cart = shopping_cart[:]
print(new_cart)