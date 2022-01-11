num = int(input("Enter a number: "))

def isPrime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if(num % i == 0):
            return False
    return True

print(isPrime(num))

#print(isPrime(2))
#print(isPrime(3))
#print(isPrime(11))
#print(isPrime(24))
#print(isPrime(19))
#print(isPrime(28))
#print(isPrime(1))
#print(isPrime(0))
#print(isPrime(57))

