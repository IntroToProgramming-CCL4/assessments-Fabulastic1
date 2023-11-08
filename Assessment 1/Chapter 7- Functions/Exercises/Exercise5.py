# Creating the function called describe_city and giving it default values
def describe_city(city, country="USA"):
    print(f"{city} is in {country}")   # printing a simple sentence for the parameter values


# Calling on the function the first time while using the default value for the country
describe_city("Los angeles")


# Calling on the function the secnond time while using the default value for the country
describe_city("New York")


# Calling on the function the third time and specifying a new city and country
describe_city("Karachi", "Pakistan")
