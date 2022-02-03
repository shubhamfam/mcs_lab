#2) Write a Python program to multiplies all the items in a list.

num_list = [1,2,3,4,5]

def multiplyList(num_list):
    multiplication = 1
    for num in num_list:
        multiplication *= num
    return multiplication

print("\nlist: ", num_list)
print("multiplication of all items: ", multiplyList(num_list))