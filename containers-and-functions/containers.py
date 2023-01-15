# DICTIONARY, LISTS, TUPLE
student = {
    'name': 'Maria',
    'course': 'SEI',
    'current_week': 7,
    'grades': (75, 85, 100),
    'address': {
        'street': '1 Infinite Loop',
        'zip_code': 95014,
        'state': 'CA',
        'country': 'USA'
    }
}

for key, value in student.items():
  if type(value) == dict:
    for k, v in value.items():
      print(f"key is {k} value is {v} ")
  # print(value)


print(student)
print(type(student))

print("\n")
print("Changing values assigned to key")
student['name'] = "Phillip"
print(student)


print("\n")
print("Adding key/value pair aka ITEM:")
student['height'] = 178
print(student)

print("\n")
print("Deleting Existing Items:")
deleted_student_height = student['height']
del student['height']
print(student)

print("\n")
print("Only since version 3.6 does Python track the insertion order of items in a dictionary - so beware if you're relying on the order items are iterated upon.")
option = 3
tup = ('name', 'James')
dict = {
    option: 'three',
    tup: 'References tup variable',
}
print(dict)

print("\n")
print("The get Method")
skills = student.get('skills')
print(skills)
# Moral of the story here, when you retreive a key, always use the .get method. ALWAYS. Why?

# if you forget the .get method:
try:
    name = student['name212121']
except KeyError:
    # except Exception:
    print("Key not found!")

"""
Error Handling:
"""
# print(10/0) Will never reach next line!
# ZeroDivisionError
print("Hello World!")


try:
    print(10/0)
# except ZeroDivisionError as e:
except Exception as e:
    print(f"Error {e}")

student = {
  'name': 'Maria',
  'course': 'SEI',
  'current_week': 7,
  'address': {
    'street': '1 Infinite Loop',
    'zip_code': 95014,
    'state': 'CA',
    'country': 'USA'
  },
} 

# del student['current_week']
# print('current_week' in student)

print("\nDictionaries - Iterating Items:")
for key, value in student.items():
  print(f"{key} = {value}")
  

# Practice Exercise Where My Things Are:
print("\nLISTS!!!")

colours = ['red', 'green', 'blue'] 


print(type(colours))
print(len(colours))
print(colours[-1])

try:
  print(colours[55])
except IndexError as e:
  print(e)

blue = colours.index('blue')
# print(green)
colours[2] = 'baby blue'
print(colours)
print("This line of code really wants to run!")

colours.append('purple')
print(colours)

# DOESN'T WORK!
print(colours.extend(['orange', 'black']))
print("\nSTORAGE:")
# print(storage)

print(colours + ['orange', 'black'])
print(colours)

odds = [1, 3, 5]
evens = [2, 4, 6]

nums = odds + evens
# print(nums)

colours = ['red', 'green', 'blue'] 
colours.insert(55, 'pink')
print(colours)

print("\npop method:")

last = colours.pop(-1)
print(last)
print(colours)

del colours[-1]
print(colours)

colours.remove('red')
print(colours)

# colours.clear()
colours = []
print(colours)

print("\nIterating Over Items in a List:")
colours = ['red', 'green', 'blue']
for index, value in enumerate(colours):
  print(f"index is {index}, value is {value}")

# Exercise(10 minutes)")
scores = [{
    'name': 'Kobe',
    'points': 24
}]
scores.append({'name': 'MJ', 'points': 63})

for player in scores:
    print(f"{player['name']} scored {player['points']} points")

print("\nList Comprehensions:")

# [<expression> for <item> in <list>]
# This reads as: I want <expression> for each <item> in <list>

print("\nTuples:")
things = ()
# print( type(things) )

hello_tuple = ('Hello', 'World')
print( type(hello_tuple) )

print("\n NEW STUFF:")
print(student.items())


# print("\nTuples Index")
# colors = ('red', 'green', 'blue')
# blue_idx = colors.index('pink')
# print(blue_idx)

print("iteration:")
colors = ('red', 'green', 'blue')
for idx, color in enumerate(colors):
  print(idx, color)


print("\nUnpacking Tuple:")
colors = ('red', 'green', 'blue')
r, g, b = colors

print("\nUnpacking Again:")
for item in student:
  # print(f"key is {key} val is {value}")
  # print( f"{key} = {val}" )
  print(item)

for item in student.items():
  # print(f"key is {key} val is {value}")
  # print( f"{key} = {val}" )
  print(item)

for key, val in student.items():
  # print(f"key is {key} val is {value}")
  # print( f"{key} = {val}" )
  print(key, val)

print("\nSLICING:")
name = 'Alexandria'
copy_of_name = name[-3:]
print(copy_of_name)

colors = ('red', 'green', 'blue')
print( colors[:2] )

colors = ['red', 'green', 'blue']
print( colors[1:] )

fruit = ('apples', 'bananas', 'oranges')
fruits_company = fruit[:]
print(fruits_company)
