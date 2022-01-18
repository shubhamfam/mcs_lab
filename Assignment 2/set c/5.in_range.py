#5. Write a Python function to check whether a number is in a given range. 

number = int(input("Enter a number: "))
range_x = int(input("Enter lower limit: "))
range_y = int(input("Enter upper limit: "))


def isInRange(number, lower, upper):
    if lower <= number <= upper:
        return True
    return False


if isInRange(number, range_x, range_y):
    print(f"{number} is in the given range: {range_x} - {range_y}")
else:
    print(f"{number} is not in the given range: {range_x} - {range_y}")