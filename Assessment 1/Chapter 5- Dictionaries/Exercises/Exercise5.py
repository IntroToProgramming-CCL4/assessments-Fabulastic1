# Creatin a list to store all the dictionaries in
pets = [
    {"kind": "Dog", "owner": "Alice"},   # storing some information about the pets by using keys and values
    {"kind": "Cat", "owner": "Bob"},
    {"kind": "Fish", "owner": "Charlie"},
    {"kind": "Bird", "owner": "David"},
]

# using a for loop to call upon the keys and values of the dictionary in the list
for pet in pets:
    kind = pet["kind"]
    owner = pet["owner"]
# Printing out all the information in the list neatly 
    print(f"This a {kind} and it's owned by {owner}")