#5.Write a NumPy program to convert the values of Centigrade degrees into Fahrenheit degrees. Centigrade values are stored into a NumPy array
import numpy as np

centigrade_arr = np.array([0, 25, 50, 75, 100], dtype=np.float)

fahrenheit_arr = (centigrade_arr * 9/5) + 32

print("\nCentigrade degrees: ", centigrade_arr)
print("\nFahrenheit degrees: ", fahrenheit_arr)