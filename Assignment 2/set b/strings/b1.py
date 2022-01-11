#1. Write a python program to print even length words in a string

string = input("Enter a string: ")

words = string.split(" ")

even_length  = [word for word in words if len(word)%2==0]

print(even_length)