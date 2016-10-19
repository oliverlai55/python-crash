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
