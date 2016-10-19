# def
# def is the function definition

def greet_user():
    """Display a simple greeting."""
    print("Hello!")

greet_user()

# """ is a docstring, describes what the function does

def greet_user(username):
    print("hello, " + username.title())

greet_user('jesse')

# Positional Argument
def describe_pet(animal_type, pet_name):
    print(animal_type + pet_name)

describe_pet('hamster', 'harry')

# Keyword Arguments
# pass name-value pair directly into the function

def describe_pet(animal_type, pet_name):
    print(animal_type + pet_name)

describe_pet(animal_type='hamster', pet_name='harry')
# order doesn't matter

# Default Values
def describe_pet(pet_name, animal_type='dog'):
    print(animal_type + pet_name)

describe_pet(pet_name='willie')
# or
describe_pet('willie')

# Return Values
THe value the function returns is called a return value

def get_formatted_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

# Optional Argument
def get_formatted_name(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = first_name + middle_anme + last_name
    else:
        full_name = first_name + last_name


# Preventing a Function from Modifying a List
function_name(list_name[:])
# the : makes a copy of the list to send to the function

print_models(unprinted_designs[:], completed_models)
# try not to make copies of list

# Passing an Arbitrary Number of Arguments
# using the asterik pack all the paramter values into a tuple
def make_pizza(*toppings):
    print(toppings)
    for topping in toppings:
        print(topping)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')


# Mixing Positional and Arbitrary Arguments
# the param that accepts an arbitrary number of arguments must be placed last in the function definition

def make_pizza(size, *toppings):
    print(size)
    for topping in toppings:
        print(topping)

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green pepper', 'extra cheese')

# Using Arbitrary Keyword Arguments
# double asteriks before the param creates an empty dictionary
def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')

# Storing Functions in Modules
# use import

# Import Specific Functions
# from module_name import funcion_name, function_name2
from pizza import make_pizza

# More info on import functions at pg 189
