import pandas as pd

df = pd.read_csv('demografia (2).csv',na_values=['NA','NaN'])
print(df.head())
print(df.describe())
print(df.info())