# Creating a dictionary named programming_glossary to store the python terms and meanings in
programming_glossary = {
    "variable": "A named storage location in memory used to store data.",
    "function": "A block of code that performs a specific task when called.",
    "for-loop": """A "for loop" is a control structure that iterates over a sequence,
executing a block of code for each item in that sequence""",
    "If statements": """An "if statement" enables conditional code execution based on a given condition""",
    "While-loop": """A "while loop" repeatedly executes code while a condition is true.""",
    # Adding five more Python terms and their meanings
    "list": "An ordered collection of items that can be of different data types.",
    "dictionary": "A data structure that stores key-value pairs.",
    "module": "A file containing Python code that can be imported and reused in other programs.",
    "syntax": "The set of rules governing the structure of statements and expressions in a programming language.",
    "iteration": "The process of repeatedly executing a block of code, often with different data or conditions."
}


# Printing each and everything in the glossary neatly with a blank line in between
for word, meaning in programming_glossary.items():
    print(f"{word}:\n{meaning}\n")
