#1. Write a Python function that takes a list and returns a new list with unique elements of the first list. 

string = input("Enter a string: ")
li = list(string)

def uniqueElements(li):
    unique = set(li)
    return list(unique)

print("input: ", li)
print("unique elements: ", uniqueElements(li))