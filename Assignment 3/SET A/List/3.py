#3) Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.

military_index = [("India", 4), ("USA", 1), ("Russia", 3), ("China", 2)]
print("\nList of tuples: ")
print(military_index)

sorted_military_index = sorted(military_index, key = lambda t: t[-1])

print("\nSorted list of tuples: ")
print(sorted_military_index)