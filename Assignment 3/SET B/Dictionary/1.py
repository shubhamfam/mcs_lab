#1. Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).

n = int(input("Enter n: "))

square_dict = dict()

for i in range(1, n+1):
    square_dict.update({i: i*i})

print("Generated dictionary: ", square_dict)