# 2) Write a Python script to add a key to a dictionary.

assignment_dict = {"Python": 3, "AI": 4, "ADC": 5, "DAA": 2}

# adding key with subscript
assignment_dict["Human Rights"] = 1
print("adding key with subscript", assignment_dict, sep="\n")

print()

# adding key-value with update method
assignment_dict.update({"SDET": 2})
print("adding key with update method", assignment_dict, sep="\n")
