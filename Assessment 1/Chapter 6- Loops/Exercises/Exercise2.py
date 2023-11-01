# Getting the age using an input function and storing the age in a variable
age = int(input("Enter yo age: "))

ticket_price = 0
# Setting the conditions using if conditions to charge
# nothing for the ticket if the age is lower than 3
if age <= 3:
    ticket_price = 0  # storing the ticket price in a variable to print out later
elif 3 < age <= 12:
    ticket_price = 12
elif age > 12:
    ticket_price = 15


# printing the ticket price for the user
print(f"Your ticket will be {ticket_price}")
