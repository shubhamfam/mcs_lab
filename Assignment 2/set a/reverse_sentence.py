def reverse_words(sentence):
    reverse_words = sentence.split()
    reverse_words.reverse()
    reverse_string = ""
    for word in reverse_words:
        reverse_string += word + " "  
    return reverse_string

string = input("Enter a string: ")
print(f"String: {string}\nReversed: {reverse_words(string)}")

#reverse_words("hi this is shubham, good morning")
#reverse_words("eat sleep binge repeat")
