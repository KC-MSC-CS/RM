import pandas as pd
import numpy as np

file_path = "medals.csv"
df = pd.read_csv(file_path)

print(df.head())

df.dropna(axis=1, inplace=True)
df = df.drop(['City'], axis=1)
# df.drop(['City'],axis=1,inplace=True)

# check if values in df are unique
print("Is Sport column unique: ",df['Sport'].is_unique)

# check if a column containes a pattern of string
ct_data = df['Sport']
ct = ct_data.str.contains('Skating')
print(ct)

# check
print(df.dtypes.value_counts())