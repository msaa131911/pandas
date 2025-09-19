

import pandas as pd

data={
    "name":["alif","pi","pi","pi"],
    "age":[22,22,22,22],
    "gender":["male","male","male","male"],
    "grade":["A","A","A","A"]
}
df=pd.DataFrame(data)
print(df)
print(df.describe(include="all"))

