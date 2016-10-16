# For loop
worldList = ['America', 'China', 'Brazil', 'Taiwan', 'Argentina']

for i in worldList:
	print(i + '.\n')
# this prints out

# Indentation
# Python uses indentation to determine when one line of cannondale
# is connected to the line above it

# Logical Error
# Syntax is valid Python code, but it does not produce the desired result because a problem occurs in its Logic

# range()
for value in range(1,5):
	print(value)
# value will not contain the last number

# Using range() to make a List of numbers
numbers = list(range(1,6))
numbers2 = list(range(1,5,2))
# skip numbers

square = []
for value in range(1,11):
	square.append(value**2)

# using min max and sum
digits = [1,2,3,4,5,6]

min(digits)
max(digits)
sum(digits)

squares = [value**2 for value in range(1,11)]

# Exercises
# 4-3
for i in range(1,21):
	print(i)

# 4-6
for i in range(1,21):
	if(i % 2 != 0):
		print(i)

# 4-7
cubes = [i**2 for i in range(3,31)]

# Slice
# a specfic group of itmes in a list
print(digits[0:3])
print(digits[:4])
# starts at the beginning of the list

print(digits[3:])
# starts from 4th, till the end of the list

# Copying a List via slice
my_food = ['pizza', 'falafel', 'carro cake']
frined_foods = my_foods[:]

print("my fav foods are")
print(my_foods)

# Tuples
# immutalbe list is called a tuple
dimensions = (200, 50)
print(dimensions[0])

for dimension in dimensions:
	print(dimension)

# you can rewrite a Tuples
dimensions = (400, 100)
