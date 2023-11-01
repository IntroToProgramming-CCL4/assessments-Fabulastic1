# making the list of sandwiches named sandwich orders
sandwich_orders = ["Tuna sandwich", "Chicken sandwich",
                   "pastrami sandwich", "Lead sandwich", "Uranium-234 sandwich"]

# Making an empty list named finished_sandwich
finished_sandwiches = []

# printing the message for running out pastrami
print("Sorry we've run out of pastrami")

# removing pastrami from the list using wile loop
while "pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("pastrami sandwich")

# making a while loop to go through the list of sandwiches
while sandwich_orders:
    # using the pop function to remove the last item of the list and store it in current orders
    current_orders = sandwich_orders.pop()
    print(f"I made your {current_orders}")  # printing current orders
    # moving the items from one list to another using append function
    finished_sandwiches.append(current_orders)

# Printing a statement in a neat way using the \n function
print("\n list of sandwiches made:")
for sandwich in finished_sandwiches:
    print(sandwich)
