import pandas as pd
import time

start = time.time()

df = pd.read_csv("data/raw/churn_data.csv")
df = df.dropna()
df["label"] = df["churn"].apply(lambda x: 1 if x == "Yes" else 0)

df.to_parquet("data/processed/cleaned_data_pandas.parquet", index=False)

print("Time (Pandas):", time.time() - start)
