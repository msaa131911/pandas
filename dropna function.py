# dropna() function
import pandas as pd

data = {
  "name": ["Alif", "Rafi", "Nila", "Tara"],
  "age": [20, None, 22, 23],
  "city": ["Dhaka", "Chittagong", None, "Sylhet"]
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

clean_df = df.dropna(inplace=False)
print("\nAfter dropna():")
print(clean_df)