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
        self.odometer_reading = 0

    def get_description_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """Print a statement shownig the car's mileage."""
        print(str(self.odomter_reading))

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_description_name())
my_new_car.read_odometer()

# Modify attribute's value directly
my_new_car.odometer_reading = 23

# Modify via method
class Car()
    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("you can't roll bacn an odometer")

my_new_car.update_odometer(23)
my_new_car.odometer()

    def increase_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

my_used_car = Car('Subaru', 'Outback', 2013)
my_used_car.update_odometer(23500)
my_used_car.update_odometer()
my_used_car.increase_odometer(100)
my_used_car.read_odometer()


# Inheritance
# When one class inherits from another, takes on all the attributes and methods of the first class. from Parent class to child class

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric cars."""
    def _init_(self, make, model, year):
        """Initialize atttributes of the parent class"""
        super()._init_(make, model, year)
# super() function is a special funciton that helps Python make connections between the parent and child class.  It tells Python to call the _init_() method from ElectricCar's parent class.  Gives ElectricCar instance all of the attributes of its parents class.

my_tesla = ElectricCar('tesla','model s', 2016)
print(my_tesla.get_description_name())

# You can override Methods from the Parent Class

# Instances as attributes
class Battery()
    def _init_(self, battery_size = 70):
        self.battery_size = battery_size

    def describe_battery(self):
        print(str(self.battery_size))

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
    """
    Initialize attributes of the parent class.
    Then initialize attributes specific to an electric car.
    """
    super().__init__(make, model, year)
    self.battery = Battery()

my_tesla.batttery.describe_battery()
