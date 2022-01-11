#2. Write a python program to accept the strings which contains all vowels
string = input("Enter a string: ")

vowels = {'a','e','i','o','u'}
vowels_in_string = set()

for char in string.lower():
    if char in vowels:
        vowels_in_string.add(char)
    
if len(vowels_in_string) == len(vowels):
    print("String accepted")
else:
    print("String not accepted")
