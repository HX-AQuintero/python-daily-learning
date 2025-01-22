selfish = "me me me"
#          01234567

# String indexes (slicing strings)

print(selfish[0])
print(selfish[1:])
print(selfish[:4])
print(selfish[0:8:1])
print(selfish[0:8:2])
print(selfish[::1])
print(selfish[-1])
print(selfish[-2])
print(selfish[::-1])

# Immutability
# selfish[0] = '100' Error!

selfish = selfish + '100'