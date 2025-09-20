#1-select specific column
#2-filter rows
#3-combine multiple conditions

import pandas as pd

data={
    "name":["John", "Anna", "Peter", "Linda","Mark","Lily","Mike","Sara"],
    "age":[28, 22, 34, 42,25,30,29,27],
    "city":["New York", "Paris", "London", "Berlin","Tokyo","Oslo","Stockholm","Istanbul"],
    "salary":[50000, 60000, 55000, 45000,50000,60000,55000,75000],
    "parfomance":["A", "B", "A", "C","B","A","C","B"]

}

df=pd.DataFrame(data)
hy_salary_age=df[(df["salary"]>50000) & (df["age"]>20) & (df["parfomance"]>"A")]
print(f"high salary:{hy_salary_age}")
other=df[(df["salary"]<50000) | (df["age"]<20) | (df["parfomance"]<"A")]
print(f"other:{other}")
