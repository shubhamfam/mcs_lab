# 1. Write a Python program to remove duplicates from a list.

num_list = [1, 2, 1, 2, 3, 4, 5, 6, 6, 7, 7]

print("Original list: ", num_list)

num_list = list(set(num_list))
print("list after removing duplicates: ", num_list)