my_tuple=(1,2,3,4,5)
new_tuple = my_tuple[1:2]
print(new_tuple)

# Another way to copy values from a tuple
x,y,z,*other = (1,2,3,4,5)
print(x,y,z,other)
print(x,y,z,*other)

print(other)
print(*other)

# Methods
my_tuple2 = (1,2,3,5,4,5,4,6,7,4,2,4,6,7,8,9,9,9)

print(my_tuple2.count(4))
print(my_tuple2.index(7))