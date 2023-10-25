places = ['canada', 'united kingdom', 'saudi arabia', 'portugal', 'japan']

# printing the list as a raw python list
print(places)

# using sort function on the list
sorted_places = sorted(places)
print(sorted_places)

# printing the original list
print(places)

# sorting list in reverse alphabetical order now
sorted_stuff = sorted(places, reverse=True)
# printing the reverse sorted list
print(sorted_stuff)

# printing the original list to show that list has been unchanged
print(places)

# Using the reverse function on the list
reversed_stuff = places.copy()  # creating a copy of the list
reversed_stuff.reverse()
# printing the reverse list
print(reversed_stuff)

# printing the original list to show that it has been unchanged
print(places)

# reversing the list again and printing it
reversed_stuff.reverse()
print(reversed_stuff)

# printing original list
print(places)

# using sort to store list in alphabetical order
places.sort()
print(places)

# showing the list has been changed
print(places)

# using sort to store list in reverse alphabetical order and printing it
places.sort(reverse=True)
print(places)

# printing list to show that it's been changed
print(places)
