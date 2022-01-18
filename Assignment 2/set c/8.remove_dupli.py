#8. Write a python program to Remove all duplicates from a given string in Python

string = input("Enter a string: ")

unique = ""

for char in string:
    if char not in unique:
        unique += char

print(unique)

