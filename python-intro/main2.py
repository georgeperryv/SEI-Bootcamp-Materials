name = 'Suresh'
age = None
names = []
student = {}
student_ssn = ()

print(bool(name))
print(bool(age))
print(bool(names))
print(bool(student))
print(bool(student_ssn))

print(8 > 8)
print(8 >= 8)
print(8 < 8)
print(8 <= 8)
print(8 == 8)
print(8 != 8)

print(False or False)
print(False and True)
print(not True)
print(not 123)
print(not [])

age = 22

if age == 22:
    pass

# age = int(input("Please enter the color "))
# print(f"color is {age} data type is {type(age)}")


numbers = [1, 2, 3, "Hi", 5]

# for i in numbers:
#     print(type(i))

# range(1,6)
# for n in range(len(numbers)):
#     print(f"{numbers[n]} = {n}")
#     if numbers[n] == 4:
#         print('found 4')

# for n in numbers:
#     print(n)


# for index, value in enumerate(numbers):
#     print(index, value)

# tup = (1, 2, 3, 4, 5)
tup = 1, 2, 3, 4, 5,  # just like const in JS

# for index, value in enumerate(tup):
#     print(index, value)

# x = 10
# while x < 9:
#     print(x)
#     x += 1


for n in range(len(numbers)):
    print(f"{numbers[n]} = {n}")
    if numbers[n] == 4:
        break
print("out of the for loop")
