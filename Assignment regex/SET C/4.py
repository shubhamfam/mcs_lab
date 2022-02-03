#4. Write a python program to put spaces between words starting with capital letters using Regex
import re

string = "ThisIsExampleString"
print("\nBefore: ", string)

words = re.findall(r'[A-Z][a-z]*', string)

string = ' '.join(words)

print("\nAfter: ", string)