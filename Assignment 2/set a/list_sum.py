#5. write a python function to sum up all the numbers in a list

numbers = [1,2,3,4,5]

def list_sum(numbers):
    sum = 0
    for num in numbers:
        sum += num
    return sum

print(list_sum(numbers))