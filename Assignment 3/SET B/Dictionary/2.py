#2. Write a Python script to merge two Python dictionaries.

dict_1 = {"Python": 3, "AI": 4, "ADC": 5, "DAA": 2}
print("\nDictionary 1: ", dict_1)

dict_2 = {"Human Rights": 1, "SDET": 2, "Cyber Security": 1}
print("\nDictionary 2: ", dict_1)

merged_dict = dict_1.copy()
merged_dict.update(dict_2)
print("\nMerged dictionary: ", merged_dict)

