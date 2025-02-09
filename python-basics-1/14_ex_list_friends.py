# Fix this code so that it prints a sorted list of all of our friends (alphabetical).
friends = ['Simon', 'Patty', 'Joy', 'Carrie', 'Amira', 'Chu']

new_friend = ['Stanley']

all_friends = friends + new_friend
all_friends.sort()
print(all_friends)

# Better solution
friends.extend(new_friend)
print(sorted(friends))