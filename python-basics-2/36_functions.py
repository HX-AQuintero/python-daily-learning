# Functions

def say_hello():
  print('helllloooooo')

say_hello()

picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]

# show_tree() NameError: name 'show_tree' is not defined

def show_tree():
  for image in picture:
    for pixel in image:
      if (pixel):
        print('*', end='')
      else:
        print(' ', end='')
    print('')

show_tree()
show_tree()
show_tree()