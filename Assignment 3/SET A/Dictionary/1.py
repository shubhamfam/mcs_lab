#1) Write a Python script to sort (ascending and descending) a dictionary by value.

assignment_dict = {"Python": 3, "AI": 4, "ADC": 5, "DAA": 2}
print("\ndictionary: ", assignment_dict)

#sorting in ascending order
sorted_assignment_dict = sorted(assignment_dict.items(), key=lambda item: item[1])
print("\nAscending order: ",dict(sorted_assignment_dict))

#sorting in descending order
sorted_assignment_dict = sorted(assignment_dict.items(), key=lambda item: item[1], reverse=True)
print("\nDescending order: ",dict(sorted_assignment_dict))
