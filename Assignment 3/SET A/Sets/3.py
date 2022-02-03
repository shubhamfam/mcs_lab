#3) Write a Python program to create set difference.

set1 = {1,2,3,4}
set2 = {3,4,5,6}
print("\nset 1: ", set1)
print("\nset 2: ", set2)

set_diff = set2 - set1

print("\nSet difference with - operator: ", set_diff)

set_diff = set2.difference(set1)

print("\nSet difference with difference method: ", set_diff)

