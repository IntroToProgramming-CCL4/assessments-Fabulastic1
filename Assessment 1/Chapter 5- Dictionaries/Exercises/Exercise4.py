# Creating a dictionary storing the rivers and country and names in
rivers = {
    "Nile": "egypt",
    "Amazon": "Brazil",
    "Yangtze": "China"
}

# Loop to print out a sentence about each river
for river, country in rivers.items():
    print(f"The {river} runs through {country}.")

# Loop to print out the name of each river
print("\nRivers:")
for river in rivers.keys():
    print(river)

# Loop for printing out the countries from the dictionary
print("\nCountries:")
for country in rivers.values():
    print(country)