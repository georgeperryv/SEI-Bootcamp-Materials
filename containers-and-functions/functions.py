# Use *args and **kwargs parameters

def foo(temp):
  pass
print(foo(20))

print("I WANT TO PRINT!")

print("\n BReaking CODE!")
def foo2(a, b, c, d, e, f, g, h, i):
  print(a, b, c)

# print(foo2('asjkdf', 'asjdkf', 'asdjkfl', 'asdjkfl'))

# Not allowed until after the code below
# add(5, 10)

# def add(a, b):
#   return a + b

def callMe():
  return "CALLED"

print(callMe())

def add(a, b):
  return a + b
  
print(add(7, 3))


print("\n*args")
def demo1(*args):
  print("This is ARGS!:")
  print( type(args) )
  for arg in args:
    print(arg)

print(demo1(1, 2, 'kenjamin', 5, (1, 2), 3, 2, 2, 1, 2, 32, 3, 4, 54, 5 ,56))

print("\n ARGS DEMO 2")
def dev_skills(dev_name, SSN, *args ):
  dev = {'name': dev_name, 'skills': list(args)}
  # args will be a tuple

  return dev

print(dev_skills('Alex', 'HTML', 'CSS', 'JavaScript', 'Python'))
# -> {'name': 'Alex', 'skills': ['HTML', 'CSS', 'JavaScript', 'Python']}



# STORE TUPLE IN VARIABLE AND THEN CONVERT TO LIST~!
#initialize tuple
aTuple = (True, 28, 'Tiger')
#tuple to list
aList = list(aTuple) 
#print list
print(type(aList))
print(aList)

def gpa_calculator(height, **kwargs,):
  print(f"Height is {height}")
  list_of_classes_taken = []
  sum = 0
  for key, val in kwargs.items():
    print(type(key))
    print(type(val))
    list_of_classes_taken.append(key)
    sum += val
  gpa = sum /len(kwargs)
  print(gpa)

print(gpa_calculator(180, english=4.0, math=3.7, chemistry=4.0))
# print(gpa_calculator(english=4.0, math=3.7, chemistry=4.0, pe=4.0, cooking=4.0))



print("\n add test:")
def add(a, b):
  return a + b
print(add(10, 100.0000))
# print(add(10, '10'))
# print(add(100))
print(add('abc', 'def'))
# print(add(10, 20, 30))