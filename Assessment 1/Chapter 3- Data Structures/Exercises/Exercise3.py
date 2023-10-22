# storing the modes of transportations in a list
transportations = ['Toyota supra', 'Nissan Silvia S15', 'Yamaha DRZ 400']
# using a for loop to print a statement for each transportation separately
for thing in transportations:        # writing a different statement for each of them
    if thing.startswith("Toyota"):
        print(f"I would absolutely love to own a {thing}, because it can be tuned very easily")
    elif thing.startswith("Nissan"):
        print(f"Now the {thing} is a thing of beauty it's mostly used to drift and i would love to own one")
    elif thing.startswith("Yamaha"):
        print(f"The {thing} is a truly special bike because it is one of the only road legal dirt bikes")

