# Exercises: Error Handling

while True:
  try:
    age = int(input('What\'s your age?:'))
    10/age
  except ValueError:
    print('Please enter a number')
    continue
  except ZeroDivisionError:
    print('Please enter age higher than zero')
    break
  else:
    print('Thank you!')
    break
  finally:
    print('Ok, I am finally done')
  print('Can you hear me?')