#6. Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters. 

string = input("Enter a string: ")

def numOfCases(string):
    upper_c = lower_c = 0
    for char in string:
        if char.isupper():
            upper_c += 1
        elif char.islower():
            lower_c += 1
    return lower_c, upper_c

lowercase, uppercase = numOfCases(string)

print(f"input has {lowercase} lowercase letters and {uppercase} upper case letters")