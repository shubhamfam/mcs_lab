#1.Write a Pandas program to add, subtract, multiple and divide two Pandas Series.
import numpy as np
import pandas as pd

arr1 = np.array([1,2,3,4,5], dtype=np.int)
arr2 = np.array([6,7,8,9,10], dtype=np.int)

series_1 = pd.Series(arr1)
series_2 = pd.Series(arr2)

print("\nSeries 1: ")
print(series_1)
print("\nSeries 2: ")
print(series_2)

print("\nAddition: ") 
print(series_1 + series_2)
print("\nSubtraction: ") 
print(series_1 - series_2)
print("\nMultiplication: ")
print(series_1 * series_2)
print("\nDivision: ") 
print(series_1 / series_2)
