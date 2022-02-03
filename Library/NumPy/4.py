'''4.Write a NumPy program to repeat all the elements three times of a given array of string

Original Array: ['CS' 'Maths' 'English' 'Hindi']

New array: ['CSCSCS' 'MathsMathsMaths ' ' EnglishEnglishEnglish ' 'HindiHindiHindi ']'''

import numpy as np

arr = np.array(['CS','Maths','English','Hindi'], dtype=np.str)

print("\nOriginal Array: ", arr)

arr1 = np.char.multiply(arr, 3)

print("\nNew array: ", arr1)