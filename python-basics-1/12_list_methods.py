# Methods

basket = [1,2,3,4,5]

# Adding
basket.append(100) # append changes the list in-place
new_list = basket
print(basket)
print(new_list)

basket.insert(4,9) # insert changes the list in-place
print(basket)
print(new_list)

basket.extend([101, 102]) # extend changes the list in-place
print(basket)
print(new_list)

# Removing
basket.pop()
basket.pop(0) # Index to delete an element from. Returns the deleted value
print(basket)

basket.remove(9) # Remove first occurrency of the value
print(basket)

new_list = basket.clear() # Deletes all the elements
print(basket)

# Querying
print(basket.index(4)) # Returns first index of value
print(basket.index(4, 0, 2)) # ValueError: value is not in list bounded by indices 0 and 2

print(4 in basket)
print(103 in basket)

# Counting
print(basket.count(5)) # Returns the number of occurrencies of the value

# Sorting
print(basket.sort()) # Sorts the list in ascending order in-place
print(basket)
print(sorted(basket)) # Creates a copy and sort the list 

print(basket.reverse()) # Reverses the list in-place
print(basket)