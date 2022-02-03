#2. Write a Python program to remove an item from a tuple.

asian_countries = ('India', 'USA', 'Japan', 'South Korea')
print("\nOriginal tuple: ", asian_countries)

#removing item from tuple
asian_countries = list(asian_countries)
asian_countries.remove("USA")
asian_countries = tuple(asian_countries)

print("\nTuple after removing item: ", asian_countries)