
import re

def match_pattern(text ,pattern):
    if re.search(pattern,text):
        return 'Match Found'
    else:
        return 'Match not found'
