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
