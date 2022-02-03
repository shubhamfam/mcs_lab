#2. Write a python Program to Remove duplicate words from Sentence

import re

def removeDuplicateWords(sentence):
    pattern = r'\b(\w+)(?:\W+\1\b)+'
 
    return re.sub(pattern, r'\1', sentence, flags=re.IGNORECASE)

sentence = "I am am a sentence sentence"

print("\nOriginal Sentence: ", sentence)
print("\nSentence after removing duplicates: ", removeDuplicateWords(sentence))