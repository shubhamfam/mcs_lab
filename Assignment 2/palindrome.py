def is_palindrome(string):
    if string == string[::-1]:
        return True
    return False    

string = input("Enter a string: ")

if is_palindrome(string):
    print(f"{string} is a palindrome")
else:
    print(f"{string} is not a palindrome")    

#print(is_palindrome("123"))
#print(is_palindrome("radar"))
#print(is_palindrome("racecar"))
