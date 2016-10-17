# input()
# the function pauses the program and waits for user to enter some text, then it stores it as a variable to make it convenient for you to work with.
# Python interprets all inputs as strings, have to use int()

# % modulo operator

# while loop, loop keeps running as long as condition is true

current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

# make program run as long as user wants
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program"
message = ""
while message != 'quit':
    message = input(prompt)

# Using a flag to see if game is still 'active'
active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)


# Break Statements
# To exit a while loop immediately without running any remaining code in the loop, regardless of the results of any conditional test, use the break statement.

prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
city = input(prompt)
    if city == 'quit':
        break
    else:
        print("I'd love to go to " + city.title() + "!")


# Using continue in a Loop
# you can use the continue statement to return to the beginning of the loop based on the result of a conditional test.

current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue

    print(current_number)
# the continue statement tells Pythong to ignore the rest of the loop and return to the beginning.


# If we want to move name from unverified names to verified list

# Start with users that need to be verified
# Verify each user until there are no more unconfirmed users.
# move each verified user into the list of confirmed users

unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_user.pop()

    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)

# Display all confirmed users.
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())


# Removing All Instances of Specific Values from a list
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']

while 'cat' in pets:
    pets.remove('cat')


# Filling a Dictionary with User Input
responses = {}

# Set a flag to indicate that polling is active.
polling_active = True

while polling_active:
    name = input("\nWhat is your name?")
    response = input("Which mountain would you like to climb")

    # Store the response in the dictionary
    responses[name] = response

    # Find out if anyone else is going to take the poll.
    repeat = input("Would you like to let another person response? (yes/no)")
    if repeat == 'no':
        polling_active = False

    print("/n === Poll Results ===")
    for name, response in responses.items():
        print(name + " would like to climb " + response)
