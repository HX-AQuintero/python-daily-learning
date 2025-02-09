# List Unpacking

a,b,c = [1,2,3]

a,b,c, *other = [1,2,3,4,5,6,7,8,9]
print(a,b,c, other)

a,b,c, *other, d = [1,2,3,4,5,6,7,8,9]
print(a,b,c, other, d)

a,b = [1,2,3,4,5,6,7,8,9]
print(a,b)