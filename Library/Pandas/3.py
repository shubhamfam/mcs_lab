#3.Write a Pandas program to select the rows the score is between 15 and 20 (consider the above dataframe).

import numpy as np
import pandas as pd

exam_data = {'name': ['Damon', 'Stefan', 'Katherine', 'Caroline', 'Emily', 'Michael', 'Matt'] ,
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5], 
'attempts': [1, 3, 2, 3, 2, 3, 1], 
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes']}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

dataframe = pd.DataFrame(data=exam_data, index=labels)

selected_rows = dataframe[dataframe['score'].between(15,20)]

print(selected_rows)