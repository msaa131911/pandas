import pandas as pd

'''
Parameter	Description
subset	কোন column গুলো চেক করবে (default: সবগুলো column)
keep	কোন ডুপ্লিকেট রাখবে তা বলে দেয়:
'first' → প্রথম occurrence বাদে বাকিগুলোকে True দেখাবে
'last' → শেষ occurrence বাদে আগেরগুলোকে True দেখাবে
False → সব ডুপ্লিকেটকে True দেখাবে
'''
data = {
    'Name': ['A', 'B', 'C', 'A', 'B', 'D'],
    'Age': [20, 21, 22, 20, 21, 23]
}

df = pd.DataFrame(data)
print(df)
#print(df.duplicated(subset='Name',keep='first'))
#print(df.drop_duplicates(subset='Name',keep='first'))
#print(df.drop_duplicates(subset='Name',keep='last'))
print(df.drop_duplicates(subset='Name',keep=False))

