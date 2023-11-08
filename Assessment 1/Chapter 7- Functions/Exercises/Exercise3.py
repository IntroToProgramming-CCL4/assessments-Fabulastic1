# Creating a function named make_shirt using the def statement
def make_shirt(size, message):
    # printing a message specifying the size and the text of the shirt
   print(f"A {size} shirt will be printed with the message: '{message}'")


# calling upon the function once using the positional arguments
make_shirt("Medium", "Hello, World!")
# calling upon the function a second time using keyword arguments
make_shirt(size="Large", message="Python Lover")

