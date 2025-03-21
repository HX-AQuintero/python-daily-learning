# Error Handling
"""
It helps prevent crashes by managing exceptions (runtime errors).
It allows programs to detect, handle, and recover from errors gracefully,
rather than stopping execution abruptly.

An exception is a type of error that occurs during program execution.
Unlike syntax errors (which prevent a script from running),
exceptions occur while the program is running.
"""
while True:
  try:
    age = int(input('What\'s your age?:'))
    10/age
  except ValueError:
    print('Please enter a number')
  except ZeroDivisionError:
    print('Please enter age higher than zero')
  else:
    print('thank you!')
    break

def division(num1, num2):
  try:
    return num1/num2
  except (TypeError, ZeroDivisionError) as err:
    print(f'Error: {err}')

print(division('1',2))
print(division(1,0))