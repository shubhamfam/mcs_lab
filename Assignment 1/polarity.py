num = int(input("Enter a number: "))

polarity = None

if num < 0:
    polarity = "Negative"
elif num > 0:
    polarity = "Positive"
else:
    polarity = "Zero"
    
print(f"{num} is {polarity}")
    