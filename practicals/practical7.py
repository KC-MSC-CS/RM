import pandas as pd

data = {'Product': ['ABC','DDD','XYZ','AAA','CCC','PPP','NNN','RRR'],
          'Price': [630,790,250,370,880,1250,550,700],
       'Discount': ['No','Yes','No','Yes','Yes','No','No','Yes']
        }
df = pd.DataFrame(data, columns = ['Product','Price','Discount'])
print(df)

# randomly select a row
df = df.sample()
# print (df)

# randomly select more than one rows
df = df.sample(n=3, replace=True)
# print (df)

print('############ Sum ########## ')
print (df.sum())
print('############ Mean ########## ')
print (df.mean())
print('############ Standard Deviation ########## ')
print (df.std())
print('############ Descriptive Statistics ########## ')
print (df.describe())