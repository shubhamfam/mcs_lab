#3.Write a NumPy program to swap rows and columns of a given array in reverse order.

'''[1234
5678
9123
4567]

row swap
[4567
9123
5678
1234]

column swap
[7654
3219
8765
4321]'''

import numpy as np

arr = np.arange(1, 10).reshape(3,3)
print(arr)


arr= arr[::-1]
print("\nRow swap in reverse: \n", arr)

print("\nColumn swap in reverse: \n", arr[::, ::-1])