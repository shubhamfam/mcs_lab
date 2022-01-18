# 4. Write a Python function to calculate the factorial of a number (a non-negative integer).
# The function accepts the number as an argument.

def factorial(num):
    if num < 0:
        return False
    if num == 1 or num == 0:
        return 1

    return num * factorial(num-1)

print(factorial(4))
print(factorial(5))
print(factorial(3))
print(factorial(4))
print(factorial(0))
print(factorial(1))
print(factorial(-4))