number = int(input("Enter a number: "))
another_number = int(input("Enter another number: "))
yet_another_number = int(input("Enter yet another number: "))

def max_of_3(number, another_number, yet_another_number):
    max = number 
    if another_number > max:
        max = another_number
    if yet_another_number > max:
        max = yet_another_number
    return max

print("max number: ", max_of_3(number, another_number, yet_another_number))