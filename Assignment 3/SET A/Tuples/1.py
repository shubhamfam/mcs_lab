#1) Write a Python program to create a tuple.
l = list()

n = int(input('Enter number of elements: '))

for i in range(n):
    ele = int(input(f'Enter {i}th element: '))
    l.append(ele)

t = tuple(l)
print("\nCreated tuple: ", t)
