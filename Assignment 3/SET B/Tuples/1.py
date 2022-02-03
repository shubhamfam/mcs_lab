#1. Write a Python program to convert a list to a tuple.

countries_list = ["India", "USA", "Japan", "South Korea"]
print("\nList: ", countries_list, "type: ", type(countries_list))

#converting list to tuple
countries_tuple = tuple(countries_list)
print("\nConverted to tuple: ", countries_tuple, type(countries_tuple))
