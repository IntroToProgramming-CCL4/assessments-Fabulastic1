# setting up a user input function to use as the number to determine their stage of life
user_input = input("Enter your age: ")
number = int(user_input)  # Writing a code to use the user input and store it in a variable to use
# Writing conditions to determine what stage of life they are in using if statements
if number <= 2:
    print("""You're a baby""")  # Using three indents in the print function to spell (You're) with a comma
elif number >= 2 and number < 4:
    print("""You're a toddler""")
elif number >= 4 and number < 13:
    print("""You're a kid""")
elif number >= 13 and number < 20:
    print("""You're a teenager""")
elif number >= 20 and number < 65:
    print("""You're an adult""")
else:
    print("""You're an elder""")