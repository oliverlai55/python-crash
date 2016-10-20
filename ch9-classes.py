# Making an object from a class is called instantiation, and you work with instances of a class.

class Dog():
    """A simple attempt to model a dog."""

    def _init_(self, name, age):
        """Initialize name and age attributes"""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command"""
        print(self.name.title() + " is now sitting")

    def roll_over(self):
        """Simulate rolling over in response to a command"""
        print(self.name.title() + " rolled over")

# __init__() method is a special method Python runs automatically whenever we create a new instance based on the Dog class

# pg 196
# variables that are accessible through instances like this are called attributes.

my_dog = Dog('willie', 6)
print(my_dog.name)
my_dog.sit()
my_dog.roll_over()


class Car():
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year

    def get_description_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_description_name())
