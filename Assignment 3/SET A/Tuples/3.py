#3) Write a Python program to check whether an element exists within a tuple.
t = (1, True, "i exist")
print("\ntuple: ", t)

ele = input("\nEnter element to check if it exists: ")

if ele in t:
    print(f'{ele} exists in the tuple')
else:
    print(f'{ele} does not exist in the tuple')