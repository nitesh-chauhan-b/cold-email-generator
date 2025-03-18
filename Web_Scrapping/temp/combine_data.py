import pandas as pd

df = pd.read_csv("collection/MS_jobs.csv")

d = df.drop(columns=["Unnamed: 0","Unnamed: 0.2","Unnamed: 0.1","Unnamed: 0.3"],inplace=True)

df = d
print(df.head())