#1. Write a python program to Count Uppercase, Lowercase, special character and numeric values using Regex
import re

string = input("\nEnter a string: ")

ucase_chars = re.findall(r"[A-Z]", string)
lcase_chars = re.findall(r"[a-z]", string)
scase_chars = re.findall(r"[$&+,:;=?@#|'<>.-^*()%!]", string)
numeric_chars = re.findall(r"[0-9]", string)


print(f"\nNo. of uppercase characters: {len(ucase_chars)}")
print(f"No. of lowercase characters: {len(lcase_chars)}")
print(f"No. of special characters: {len(scase_chars)}")
print(f"No. of numeric characters: {len(numeric_chars)}")