pizza_toppings = []  # creating an empty list to store all the pizza toppings in

# using a while loop to ask for the toppings infinitely unless the user types quit
while True:
    topping = input("Enter a topping for your pizza (or type 'quit' to finish)")


    if topping.lower() == 'quit':
        break   # Exiting the loop if the user types quit by using break statement


    print(f"I'll add {topping} to your pizza.")
    pizza_toppings.append(topping)


print("Your pizza will have the following toppings")
for topping in pizza_toppings:
    print(topping)
    