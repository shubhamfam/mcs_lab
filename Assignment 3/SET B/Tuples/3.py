#3. Write a Python program to slice a tuple.
countries_tuple = ("India", "USA", "Japan", "South Korea")

slice1 = countries_tuple[2:4]
print("\nTuple Items from 2 to 3 = ", slice1)

slice2 = countries_tuple[3:]
print("\nTuple Items from 3 to End = ", slice2)

slice3 = countries_tuple[:4]
print("\nTuple Items from Start to 3 = ", slice3)

slice4 = countries_tuple[:]
print("\nTuple Items from Start to End = ", slice4)
