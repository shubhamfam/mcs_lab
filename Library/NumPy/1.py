#1.Write a NumPy program to create an array of 10 zeros,10 ones, 10 fives.

import numpy as np

arr = np.zeros(10, dtype=np.int)
print("\nArray of 10 zeros: ", arr)

arr2 = np.ones(10, dtype=np.int)
print("\nArray of 10 ones: ", arr2)

arr3 = np.ones(10, dtype=np.int)*5
print("\nArray of 10 ones: ",arr3)