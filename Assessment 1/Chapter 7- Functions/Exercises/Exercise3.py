# Creating a function named make_shirt using the def statement
def make_shirt(shirt):
    # printing a message specifying the size and the text of the shirt
    print("So your shirt size will be", shirt, "and the text printed on it will be", text)


# calling upon the function once using the positional arguments
size = input("What size shirt do you want: ")
# calling upon the function a second time using keyword arguments
text = input("What message do you want printed on your shirt: ")
make_shirt(size)
