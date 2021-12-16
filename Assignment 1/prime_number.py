def is_prime(num):
    if num == 2:
        return True
    
    for factor in range(2, num):
        if num % factor == 0:
            return False
    
    return True

print(is_prime(2))
print(is_prime(3))
print(is_prime(4))
print(is_prime(11))