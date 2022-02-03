#2. Write a python program to find the most occurring number in a string using Regex

import re

string = '11aa333333bb99'

nums = re.findall('[0-9]+', string)

num_str = ''
for num in nums:
    num_str += num

num_frequency = dict()

for dig in num_str:
    if dig in num_frequency:
        num_frequency[dig] += 1
    else:
        num_frequency[dig] = 1

most_occurring_num = max(zip(num_frequency.values(), num_frequency.keys()))[1]

print("\nString : ", string)
print("\nMost Ocurring Number: ", most_occurring_num)


