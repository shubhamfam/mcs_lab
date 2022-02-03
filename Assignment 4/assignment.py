'''
#1
file = open('./assignment.txt', 'w')
file.close()

#2
file = open('./assignment.txt', 'r')
file.close()
'''
#3
file = open('./assignment.txt', 'r')
pos = file.tell()
print("Current file pointer: ",pos)
file.close()
'''
#4
file = open('assignment.txt', 'r')
print("\nFile content: ", file.read())
file.close()


#5
file = open('assignment.txt', 'a+')
print("\nbefore appending: ", file.read())
file.write('\nappending more text to file')
file.seek(0)
print("\nafter appending: ", file.read())
file.close()


#6 Q6) Write a Python program to count the number of lines in a text file.
file = open('assignment.txt', 'r')

lines = file.readlines()
num_of_lines = len(lines)
print("\nNumber of lines: ", num_of_lines)


#Q7) Write a Python program to read a random line from a file.
import random

file = open('assignment.txt', 'r')
lines = file.readlines()
random_line = random.choice(lines)
print("\nrandom line from the file: ", random_line)
file.close()


#Q9) Write a Python program to read a file line by line store it into an array.
lines = []
with open('assignment.txt', 'r') as file:
    for line in file:
        lines.append(line)

print("\nlines array",lines)

#Q10) Write a Python program to write a list content to a file.
list_content = ['Hello Good Afternnon', 'i am text file', 'nice to meet you human', '3000']

with open('assignment.txt', 'w+') as file:
    for line in list_content:
        file.write(line+"\n")
    file.seek(0)
    print(file.read())

#Q11) Count the total number of upper case, lower case, and digits used in the text file.

ucase_count = lcase_count = digit_count = 0

file = open('assignment.txt', 'r')

content = file.read()

for char in content:
    if char.isupper():
        ucase_count += 1
    elif char.islower():
        lcase_count += 1
    elif char.isdigit():
        digit_count += 1

print(f"Uppercase Count: {ucase_count}, \nLowercase Count: {lcase_count},\ndigits count: {digit_count}")


#Q12) Read the contents of file in reverse order.
file = open('assignment.txt', 'r')
content = file.readlines()

for line in reversed(content):
    print(line)

file.close()'''