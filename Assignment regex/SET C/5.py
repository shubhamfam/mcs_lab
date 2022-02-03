#5. Write a python to Check whether a string starts and ends with the same character or not
import re 

pattern = r'^[a-z]$|^([a-z]).*\1$'

def check(string):
    if(re.search(pattern, string)):
        print(f"\n\'{string}\' starts and ends with the same character")
    else:
        print(f"\n\'{string}\' does not starts and ends with the same character")

check('aabbc')
check('aabba')
check('dabbd')