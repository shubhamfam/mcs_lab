#1. Write a Python program to check if a set is a subset of another set.

animals = {"lion", "tiger", "dog", "cat", "elephant"}
cute_animals = {"cat", "dog"}
birds = {"eagle", "sparrow", "peacock"}

print("\nanimals: ", animals)
print("\ncute animals: ", cute_animals)
print("\nbirds: ",birds)

print("\nCute animals is subset of animals: ", cute_animals.issubset(animals))
print("\nBirds is subset of animals: ", birds.issubset(animals))
