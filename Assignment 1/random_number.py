import random

print("Generating a random number........")

print(random.randint(1, 100))

print(random.random())

random = [random.randint(1, 100) for i in range(1, 10)]
print(random)

