#3. write a python to remove ith character from a string
string = input("Enter a string: ")

index = int(input("Enter index to remove character: "))

string = string.replace(string[index], "")

print(string)
