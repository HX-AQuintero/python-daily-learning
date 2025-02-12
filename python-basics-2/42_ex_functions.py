# Exercise Functions
# Highest Even: Write a function to find the highest even number from the list.

def highest_even(li):
  even_numbers = set()
  for num in li:
    if num % 2 == 0:
      even_numbers.add(num)
  return max(even_numbers)


# Shorter solution
def highest_even(li):
  return max({num for num in li if num % 2 == 0})

print(highest_even([1,2,3,4,5,6,7,8,90]))
print(highest_even([100,202,301,-60,78,90]))