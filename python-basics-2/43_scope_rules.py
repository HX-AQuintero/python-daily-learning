a = 1

def confusion():
  a = 5
  return a

print(a) # 1
print(confusion()) # 5


print(confusion()) # 5
print(a) # 1

def parent():
  a = 10
  def confusion():
    return a
  return confusion()

print(parent()) # 10
print(a) # 1

def parent2():
  def confusion():
    return sum
  return confusion()

print(parent2()) # <built-in function sum>

# 1 - Start with local
# 2 - Parent local
# 3 - Global
# 4 - Built-in python functions
