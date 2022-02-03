#1. Write a Python program to match a string that contains only upper and lowercase letters, numbers, and underscores.

import re

def match_pattern(text ,pattern):
    if re.search(pattern,text):
        return 'Match Found'
    else:
        return 'Match not found'

pattern = '^[a-zA-Z0-9_]*$'

print()
print(match_pattern('thisISAvalidtext3000', pattern))
print(match_pattern('$$$this is not valid &&&', pattern))
print(match_pattern('7777373', pattern))