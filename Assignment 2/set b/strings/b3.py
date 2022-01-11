#3. Write a python program to Count the Number of matching characters in a pair of string
string_1 = input("Enter a string: ")#"shubham"
string_2 = input("Enter another string: ")#"awesome"

matching_chars = set()

for char in string_1:
    if char in string_2:
        matching_chars.add(char)


print("Matched characters: ", len(matching_chars))
print(matching_chars)

