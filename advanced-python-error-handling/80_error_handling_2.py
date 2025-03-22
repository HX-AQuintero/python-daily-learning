# Error Handling 2
"""
The raise statement is used to manually trigger an exception in Python.
You use raise when you want to stop execution or signal something went wrong,
even if the code didn’t "naturally" fail. It's like saying:

“Even though everything seems fine, I'm telling you this situation is bad.”
"""
while True:
  try:
    age = int(input('What\'s your age?:'))
    10/age
    raise ValueError('Hey cut it out')
  except ZeroDivisionError:
    print('Please enter age higher than zero')
    break
  else:
    print('Thank you!')
    break
  finally:
    print('Ok, I am finally done')
  print('Can you hear me?')