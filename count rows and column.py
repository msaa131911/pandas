import pandas as pd

d = {'col1': [1, 2, 3, 4, 7], 
'col2': [4, 5, 6, 9, 5], 
'col3': [7, 8, 12, 1, 11], 
'col4': [1, 3, 2, 4, 6],
'col5': [1, 3, 2, 4, 6]}

df = pd.DataFrame(data=d,index=["row1","row2","row3","row4","row5"])

count_rows = df.shape[1] #count rows
count_columns = df.shape[0] #count columns
print(count_rows)
print(count_columns)

