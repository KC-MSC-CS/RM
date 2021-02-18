import pandas as pd
import numpy as np

file_path = ""
df = read_csv(file_path)
df.dropna(axis=1, inplace=True)
df = df.drop(['group'], axis=1)
print(df.head())
# df.drop(['group'],axis=1,inplace=True)

# check if values in df are unique
print(df['Sr No']).is_unique()

# index the df by serial no
df = df.set_index('Sr no')
print(df)

print(df.loc[1])
print(df.loc[4])

# check if a column containes a pattern of string
ct_data = df['group']
ct = ct_data.str.contains('ctrl')
print(ct)

# check
print(df.dtypes.value_counts())

print(df.loc[2:, 'Sr No'].head(4))
extr = df['nos'].str.extract(r'^(\d{4})', expand=True)
df['nos'] = pd.to_numeric(extr)
print(df['nos'].dtype)

df.columns = ['a', 'b', 'c', 'd']
