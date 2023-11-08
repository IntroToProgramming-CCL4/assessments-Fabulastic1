# Using the default parameter to print a shirt of large size and a specific message
def make_shirt(size="Large", message="I love Python"):
    print(f"A {size} shirt will be printed with the message: '{message}'")

# Creating a large shirt with the default message
make_shirt()

# Creating a medium shirt with the default message
make_shirt(size="Medium")

# Creating a custom-sized shirt with a different message
make_shirt(size="Small", message="Hasta la vista!")
