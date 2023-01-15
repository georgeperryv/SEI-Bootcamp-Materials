# this is a comment
"""
this is a multi line
comment,
also known as doc string
"""

# snake_case
my_number = 15
print(my_number)
print(type(my_number))

is_true = True
print(type(is_true))

name = "Suresh"
print(type(name))

pi = 3.14
print(type(pi))

my_complex = 3 + 4j
print(type(my_complex))

my_none = None
print(type(my_none))

num = 10
# num = num + 1
num += 1
print(num)

# num = num / 5
num /= 5
print(type(num))

age = 15
b = 'Beer' if age >= 21 else 'Milk'
print(b)

my_string_1 = 'This is a String'
my_string_2 = "This is a String"
my_string_3 = '''
This 
is 
a 
string
'''

print(my_string_1)
print(my_string_2)
print(my_string_3)

hello = 'hello'
world = 'world'
result = hello + world
print(result)
print('The result is ' + result)

print(f"The result us {result}")

my_str = "ace of spades"
# print(my_str[-4])
print(type(my_str.split(" ")))
print(list("Hello world"))
print(my_str.index("a"))
print(my_str.upper())
print(my_str.lower())
# print(my_str.replace('ace', "Hello"))

# print("ace1" in my_str)

print(id(my_str))
print(id(my_str.replace('ace', "Hello")))
# this will not work
# x = 100
print(len(my_str))

# num = 25
# msg = f"There are " + {num} + " tacos"
# print(msg)
