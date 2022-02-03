# 2. Write a Python program to check a list is empty or not.

list = []
not_empty_list = [1, 2, 3, "i am not empty"]


def isEmptyList(list):
    if not list:
        return True
    else:
        return False

print(f'\n{list} is empty: {isEmptyList(list)}')
print(f'\n{not_empty_list} is empty: {isEmptyList(not_empty_list)}')