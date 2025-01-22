# 1 Create a user profile for your new game.
# This user profile will be stored in a dictionary with keys: 'age', 'username', 'weapons', 'is_active' and 'clan'
my_user = {
  'age': 28,
  'username': 'Devilblue',
  'weapons': [
    'Leviathan Axe',
    'Guardian Shield',
    'Bare-Handed Attacks',
    'Blades of Chaos',
    'Talon Bow'],
  'is_active': True,
  'clan': None
}

# 2 iterate and print all the keys in the above user.
print('keys: ', my_user.keys())

# 3 Add a new weapon to your user
my_user['weapons'] + ['Arms of Sparta']

# 4 Add a new key to include 'is_banned'. Set it to false
my_user['is_banned'] = False

# 5 Ban the user by setting the previous key to True
my_user.update({'is_banned': True})

# 6 create a new user2 by copying the previous user and update the age value and username value.
other_user = my_user.copy()
other_user.update({'age': 34, 'username': 'Fighter3000'})

print('my user is: ', my_user)
print('the other user is: ', other_user)