# List
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[-1])
# the -1 gives you the last item in list
# -2 gives you 2nd from last

bicycles[1] = "hello"
# modifying list item

# append() adds item to end of list
bicycles.append('123')

# insert() add item to specific position
bicycles.insert(0, 'ducati')

# del()  removing items
del bicycles[0]

# pop() method removes the last item in a list
# but it lets you work with that item after removal
bicycles.pop()
bicycles.pop(0)
# removes first item
"the first item is" + bicycles.pop[0]

# remove() remove by value in list
bicycles.remove('123')

too_expensive = 'ducati'
bicycles.remove(too_expensive)

# 3-4 Exercises
peopleList = ['mike', 'david', 'steph','chancie']
for i in range(0, len(peopleList)):
    print('welcome' + peopleList[i])

print(peopleList.pop(1) + ' will not be joining us')
peopleList.insert(1, 'Dennis')

print('however, ' + peopleList[1] + ' will be joining us instead' )

print(peopleList)

peopleList.insert(0, "johnny")
peopleList.insert(int((len(peopleList)/2)), 'mary')
peopleList.append('Howerad')

print(peopleList)

#  sort() is for sorting a List
bicycle.sort()
# alphabetaical order

bicycle.sort(reverse=True)
# revserse order

#  sorted() Sorting a list temporarily , just for display
sorted(bicycle)

#  reverse() to reveser the order of the list
