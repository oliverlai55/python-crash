cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# checking multiple conditions
age_0 = 22
age_1 = 18
age_0 >= 21 and age_1 >= 21
# can use 'or'

# Checking if value is in a List
# use 'in'
'bmw' in cars
# True


# Can also use 'not in'
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(user.title() + ", you can post a response if you wish.")

# if-elif-else Chain
age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
elif age >= 65:
    price = 5

# Testing Multiple Conditions
# The if-elif-else chain is powerful, but it’s only appropriate to use when you just need one test to pass. As soon as Python  nds one test that passes, it skips the rest of the tests. This behavior is bene cial, because it’s ef cient and allows you to test for one speci c condition.
# However, sometimes it’s important to check all of the conditions of interest. In this case, you should use a series of simple if statements with no elif or else blocks. This technique makes sense when more than one condi- tion could be True, and you want to act on every condition that is True.

#  Python doesn’t run any tests beyond the  rst test that passes in an if-elif-else chain.

requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms")
if 'pepperoni' in requested_toppings: print("Adding pepperoni.")
if 'extra cheese' in requested_toppings: print("Adding extra cheese.")
