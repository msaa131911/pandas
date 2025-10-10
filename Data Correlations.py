import pandas as pd
'''
কোন পদ্ধতিতে correlation বের করবে:
'pearson' → ডিফল্ট, লিনিয়ার সম্পর্ক
'kendall' → র‍্যাঙ্ক ভিত্তিক সম্পর্ক
'spearman' → র‍্যাঙ্ক correlation
'''
data = {
    'Math': [80, 85, 88, 92, 95],
    'Science': [78, 82, 90, 94, 96],
    'English': [60, 65, 70, 72, 75]
}

df = pd.DataFrame(data)
print(df)
print(df.corr(method='pearson'))
