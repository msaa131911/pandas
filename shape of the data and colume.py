#1-shape of the data
#2-colume of the data

import pandas as pd 

data={
    "name":["John", "Anna", "Peter", "Linda","Mark","Lily","Mike","Sara"],
    "age":[28, 22, 34, 42,25,30,29,27],
    "city":["New York", "Paris", "London", "Berlin","Tokyo","Oslo","Stockholm","Istanbul"]
}
df=pd.DataFrame(data)
print(df)
print(f"shape of the data is {df.shape}")
print(f"columns of the data is {df.columns}")

"""
print(f"index of the data is {df.index}")
print(f"head of the data is {df.head()}")
print(f"tail of the data is {df.tail()}")
print(f"describe of the data is {df.describe()}")
print(f"info of the data is {df.info()}")
"""