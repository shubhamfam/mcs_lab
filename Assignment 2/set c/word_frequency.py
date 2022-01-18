#3. Write a python program Words Frequency in String Shorthands

string = input("Enter a string: ")

word_counts = {word: string.count(word) for word in string.split()}

print(word_counts)

