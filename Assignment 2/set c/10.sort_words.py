#10. Write a Python program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically

words = input("Enter a string: ")

word_list = words.split("-")
word_list.sort()

words = ""

print("-".join(word_list))