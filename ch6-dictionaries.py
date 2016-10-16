alien_0 = {'color': 'green', 'points': 5}
print(alien_0[color])

# Dictionary is a collection of key-value pairs

new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!")

# Adding new key-value pairs
alien_0['x_position'] = 0
alien_o['y_position'] = 25

# You can start with empyt dictionary and then add more
alien_0 = {}
alien_0['a': 1]

# Modify values in Dictionary by assigning it new value

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("original x-position: " + str(alien_0['x_position']))

# move to the right and determine how far to move the alien based on its current speed

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_0['x_position'] = alien_0['x-position'] + x_increment

# use del to remove key-value pair
del alien_0['points']

# Looping through all Key-Value pairs
user_0 = {
    'username': 'abc',
    'first': 'a',
    'last': 'c',
    }

for key, value in user_0.items():
    print('\nKey: ' + key)
    print('Value: ' + value)

# can use k, v instead of key, value
# items() method returns a list of key-value pairs

# Looping Through all the Keys in a Dictionary
for key in user_0.keys()
    print('Key: ' + key)

# this pull all the keys, it is the default behavior for Python
# for key in user_0: is the same as for key in user_0.keys()

favorite_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

friends = ['phil', 'sarah']
for name in favorite_language.keys():
    print(name.title())

    if name in friends:
        print("your fav language is " + favorite_language[name])

# To get order use sorted()
for name in sorted(favorite_language.keys()):
    print(name.title())

# Looping through all values in a dictionary
for language in favorite_language.values()
    print(language.title())

# Wrap set() around a list that contains duplicate items, use set() to pull out the unique languages in favorite_languages.values(), so 'python' is only returned once

# Nesting

# A List of Dictionaries
aliens = []

# make 30 aliens
for i in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# Show the first 5 aliens:
for alien in aliens[:5]:
    print(alien)

# Modify first 3 aliens
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = '10'
        alien['speed'] = 'medium'
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

# Show how many alines have been created.
print(len(aliens))


# A List in a Dictionary
