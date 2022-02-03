#3. Write a python to| Remove all characters except letters and numbers PROGRAMS

import re

string = '$##this is a sentence !!!'

clean_string = re.sub('\W+', '', string)

print("\nOriginal string: ", string)
print("\nCleaned string: ", clean_string)

