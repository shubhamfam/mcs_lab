#1. Write a Python program to find sequences of lowercase letters joined with a underscore

import re

def match_pattern(text ,pattern):
    if re.search(pattern,text):
        return 'Match Found', re.findall(pattern,text)
    else:
        return 'Match not found'


pattern = '^[a-z]+_[a-z]+$'

print()
print(match_pattern('aaa_aaa', pattern))
print(match_pattern('a_c', pattern))
print(match_pattern('aaa_Zaa', pattern))