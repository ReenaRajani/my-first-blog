print('Hello World!')

# a= 4
# b= 2

def conditionalfunction():
  a = input('Enter value of a ')
  b = input('Enter the value of b ')
  if  a > b:
    print(' a is greater than b ')
  elif a < b:
    print( ' a is less than b ')
  else:
    print(' a and b are equal ')

conditionalfunction()

def sayhello(name):
  print(' hello ' + name)


name = input('What is your name ?')
sayhello(name)

girls = ['Reena' , 'Julie' , 'Sarah' , 'Michela' , 'Jo']

for name in girls:
  sayhello(name)


for i in range(1, 6): # prints  1,2,3,4,5 does not print 6
  print(i)