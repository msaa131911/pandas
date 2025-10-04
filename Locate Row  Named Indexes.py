import pandas as pd
x={
    "name":["John","Anna","James","Linda"],
    "age":[28,22,35,32],
    "city":["New York","Paris","London","Berlin"]
}
y=pd.DataFrame(x,index=["a","b","c","d"])

print(y.loc["a"]) #refer to the named index

print(y.iloc[0]) #refer to the index position 
