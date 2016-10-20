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

# Returning a dictionary
def build_person(first_name, last_name):
    person = {'first': first_name, 'last': last_name}
    return person

musician = build_person('jimi', 'hendrix')
print(musician)


def build_person(first_name, last_name, age=''):
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix', age=27)


# Using Function with a while loop
def get_formatted_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()

while True:
    print("name?")
    print("enter 'q' at any time to quit")

    f_name = input("First anme: ")
        break

    l_name = input("last name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(formatted_name)

# Passing a List
def greet_users(names):
    for name in names:
        msg = name.title()
        print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)

# Modifying a List in a function
# start with designs that need to be printed
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

# Simulate printing each design, until none are left
# Move each design to completed_models after printing
while unprinted_designs:
    current_design = unprinted_designs.pop()

    # Simulating creating a 3D print from the design
    print("Printing model: " + current_design)
    complete_models.append(current_design)

# Display all completed models
for completedModel in completed_models:
    print(completedModel)


# Refactoring
def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()

        completed_models.append(current_design)

def show_completed_models(completed_models):
    for completedModel in completed_models:
        print(completedModel)


print_model(['iphone case', 'robot pendant', 'dodeceron'])
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
