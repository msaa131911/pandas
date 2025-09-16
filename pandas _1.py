import pandas as p
data={
    "name":["ram","abid","alif"],
    "age":[10,20,30],
    "city":["pabna","dhaka","sylhet"]
    
}
df=p.DataFrame(data)
print(df)

df.to_csv("data.csv",index=False)