'''2.Write a Pandas program to select the 'name' and 'score' columns from the following DataFrame.

exam_data = {'name': ['Damon', 'Stefan', 'Katherine', 'Caroline', 'Emily', 'Michael', 'Matt'] 'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5], 'attempts': [1, 3, 2, 3, 2, 3, 1], 'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes']}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

Expected Output: Select specific columns: name score a Anastasia 12.5 b Dima 9.0 c Katherine 16.5 d Carloine np.nan

e Emily 9

f Michael 20

g Matt 14.5'''

import numpy as np
import pandas as pd

exam_data = {'name': ['Damon', 'Stefan', 'Katherine', 'Caroline', 'Emily', 'Michael', 'Matt'] ,
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5], 
'attempts': [1, 3, 2, 3, 2, 3, 1], 
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes']}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

dataframe = pd.DataFrame(data=exam_data, index=labels)

print(dataframe[['name', 'score']])
