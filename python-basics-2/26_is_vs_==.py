# Is vs. ==
# == checks for equality of value.
print(True == 1) # True == bool(1)
print('' == 1) # False == bool(1)
print([] == 1) # False == bool(1)
print(10 == 10.0) # 10 == int(10.0)
print([] == []) # False == False
print([1,2,3] == [1,2,3])

# is checks if the location in memory, where the value is stored, is the same.
print(True is 1) # No, True is True
print('' is 1) # No, '1' is '1'
print([] is 1) # No, [] is not [] (different memory locations)
print(10 is 10.0) # No, 10 is 10
print([1,2,3] is [1,2,3]) # No, they live in different memory location

a = [1,2,3]
b = a
print(a is b)