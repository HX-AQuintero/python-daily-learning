# Common list patterns

basket = ['a', 'x', 'b', 'c', 'd', 'e', 'd']
basket.sort()
basket.reverse()
print(basket[::-1]) # Creates a new list

# Range
print(list(range(101)))
print(list(range(1,100)))

# Join
sentence = ' '
new_sentence = sentence.join(['hi', 'my', 'name', 'is', 'Bond'])

# A better way
new_sentence2 = ' '.join(['hi', 'my', 'name', 'is', 'Bond'])

print(new_sentence2)