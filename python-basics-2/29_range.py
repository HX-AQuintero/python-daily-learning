# Range
"""
Return an object that produces a sequence of integers from start (inclusive) to stop (exclusive) by step.
"""
for item in range(100):
  print(f'{item} hello world!')

for _ in range(0, 10, 2):
  print(_) # 0 2 4 6 8

for _ in range(10, 0, -2):
  print(_) # 10 8 6 4 2

print(list(range(10))) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]