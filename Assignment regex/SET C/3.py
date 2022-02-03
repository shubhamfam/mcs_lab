#3. Write a python Regex to extract maximum numeric value from a string

import re

string = '11aa333333bb99'

nums = re.findall('[0-9]+', string)

nums = map(int, nums)

print("\nString: ", string)
print("\nMaximum numeric value in string: ", max(nums))