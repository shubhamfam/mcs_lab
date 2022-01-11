#3. Write a Python function to check whether a number is perfect or not.

num = int(input("Enter a number: "))

def isPerfect(num):
    sum = 0
    for factor in range(1, num//2 + 1):
        if num % factor == 0:
            sum += factor
    
    if sum == num:
        return True
    return False


if isPerfect(num):
    print(num, "is a perfect number")
else:
    print(num, "is not a perfect number")

#print(isPerfect(12))
#print(isPerfect(6))
#print(isPerfect(28))
#print(isPerfect(496))
#print(isPerfect(841))
#
#for i in range(1, 10000):
#    if isPerfect(i):
#        print(i , " ")