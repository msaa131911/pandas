#fillna() function

import pandas as pd

data = {
  "name": ["Alif", "Rafi", "Nila", "Tara"],
  "age": [20, None, 22, 23],
  "city": ["Dhaka", "Chittagong", None, "Sylhet"]
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

filled_df = df.fillna({"age": 20, "city": "Dhaka"})
print("\nAfter fillna():")
print(filled_df)