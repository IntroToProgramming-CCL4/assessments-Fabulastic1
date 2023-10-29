# Creating a dictionary named programming_glossary to store the variables and meanings in
programming_glossary = {
    "variable": "A named storage location in memory used to store data.",
    "function": "A block of code that performs a specific task when called.",
    "for-loop": """A "for loop" is a control structure that iterates over a sequence,
executing a block of code for each item in that sequence""",
    "If statements": """An "if statement" enables conditional code execution based on a given condition""",
    "While-loop": """A "while loop" repeatedly executes code while a condition is true.""",
}


# Printing each and everything in the glossary neatly with a blank line in between
for word, meaning in programming_glossary.items():
    print(word + ":")
    print(meaning + "\n")
