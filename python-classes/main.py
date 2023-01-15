# What is Encapsulation?

# https://pynative.com/wp-content/uploads/2021/08/encapsulation_python_class.jpg

# create a list
nums = [1, 2, 3]
# print(dir(nums))

# Define a class
# https://res.cloudinary.com/practicaldev/image/fetch/s--2uuFQblw--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://thepracticaldev.s3.amazonaws.com/i/va7qakwzwhwzy2oi975w.png


class Car:
    def __init__(self):
        self.wheels = 4
        self.make = 'Toyota'

    def move(self):
        print('moving')

    # Method Overiding
    def __str__(self):
        return f"Car has {self.wheels} wheels and is a {self.make}."


kens_camry = Car()
print(kens_camry.move())
# print(kens_camry.move())
# print(kens_camry.wheels)
# print(kens_camry.make)
'''
Python __repr__() function returns the object representation in
string format. This method is called when repr() function is invoked
on the object. If possible, the string returned should be a valid
Python expression that can be used to reconstruct the object again.
'''


class SportsTeam():
    def __init__(self, name):
        self.name = name


warriors = SportsTeam('warriors')
# Packaged methods that come with the SportsTeam class.
print(dir(warriors))


class Dog():
    # class attribute
    next_id = 1

    def __init__(self, name, age=0):
        self.name = name
        self.age = age
        Dog.next_id += 1
        self.id = Dog.next_id

    def bark(self):
        print(f'{self.name} says woof!')

    def __str__(self):
        return f'Dog {self.id} named {self.name} is {self.age} years old.'

    @classmethod
    def get_total_dogs(cls):
        # cls represents Dog class
        return cls.next_id-1


# Decorators:
'''

def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner


def ordinary():
    print("I am ordinary")


We can use the @ symbol along with the name of the decorator function and place it above the definition of the function to be decorated. For example,


@make_pretty
def ordinary():
    print("I am ordinary")


is equivalent to


def ordinary():
    print("I am ordinary")


ordinary = make_pretty(ordinary)

This is just a syntactic sugar to implement decorators.
'''


spot = Dog('Spot')
print("\nThis is SPOT")
print(spot)
# print(spot.name)
# print(spot.age)

lassie = Dog('Lassie')
# print(lassie.name)
# print(lassie.age)
print(lassie)

# class methods are called on the class, not an instance
print(Dog.get_total_dogs())  # -> 2
# print(Dog.next_id-1)

# Inheritance
# Pass in superclass as argument:


class ShowDog(Dog):
    # # Add additional parameters AFTER those in the SUPERCLASS!
    def __init__(self, name, age=0, total_earnings=0):
        # Always call the SUPERCLASS's __INIT__ first:
        super().__init__(name, age)
        self.total_earnings = total_earnings

    # Add prize money method:
    def add_prize_money(self, amount):
        self.total_earnings += amount


winky = ShowDog('Winky', 3, 1000)
print(winky)
winky.bark()
print(winky.total_earnings)  # -> 1000
winky.add_prize_money(500)
print(winky.total_earnings)  # --> 1500
# print("\nExercise - Create a Class (15 min):")
'''
class Vehicle:
    def __init__(self, vin, make, model):
        self.vin = vin
        self.make = make
        self.model = model
        self.running = False

    def start(self):
        self.running = True

    def stop(self):
        self.running = False

    def __str__(self):
        return f"Vehicle {self.vin} is a {self.make} model {self.model}"


kens_car = Vehicle('88GOAT', 'Lexus', 'CT250')
print(kens_car.running)  # -> False
kens_car.start()
print(kens_car.running)

kendricks_plane = Vehicle('143143143', 'Boeing', '747-B')
print(kendricks_plane.vin, kendricks_plane.make, kendricks_plane.model)
print(kens_car)
print(kendricks_plane)
'''
