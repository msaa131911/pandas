#info() function is used to get the information about the dataset.

import pandas as pd

df=pd.read_csv("C:\\Users\\MS AA\\Downloads\\orders.csv")
print(df.info())