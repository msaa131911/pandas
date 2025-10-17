import pandas as pd

data = {
    "Team": ["A", "A", "B", "B", "C", "C"],
    "Runs": [250, 300, 180, 200, 400, 350],
    "Wickets": [8, 9, 6, 5, 10, 8]
}

df = pd.DataFrame(data)

# groupby + agg
result = df.groupby("Team").agg({
    "Runs": ["mean", "max"],
    "Wickets": "sum"
})
print(result)
