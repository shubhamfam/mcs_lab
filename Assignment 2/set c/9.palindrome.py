#9. Write a Python function that checks whether a passed string is palindrome or not. 
import re


string = input("Enter a string: ")

def isPalindrome(string):
    if string == string[::-1]:
        return True
    return False

if isPalindrome(string):
    print(f"{string} is a palindrome")
else:
    print(f"{string} is not a palindrome")