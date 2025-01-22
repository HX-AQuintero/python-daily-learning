username = input('Enter your username: ')
password_length = len(input('Enter your password: '))
encryption = '*' * password_length

print(f'{username}, your password, {encryption}, is {password_length} letters long')
