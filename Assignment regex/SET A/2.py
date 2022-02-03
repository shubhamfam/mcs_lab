#2. Write a python program to Check if String Contain Only Defined Characters using Regex

import re

def match_pattern(text ,pattern):
    if re.search(pattern,text):
        return 'Match Found'
    else:
        return 'Match not found'

pattern = '^[0-9]+'

print(match_pattern('0aa', pattern))
print(match_pattern('8aa', pattern))
print(match_pattern('Aaa', pattern))