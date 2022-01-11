#2. Write a python program Check if a Substring is Present in a Given String

string = input("Enter a string: ")
substring = input("Enter a substring: ")

if string.find(substring) != -1:
    print(f"\"{substring}\" is present in \"{string}\"")
else:
    print(f"\"{substring}\" is not present in \"{string}\"")