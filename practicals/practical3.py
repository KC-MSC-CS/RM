#Pract 3 -descriptive statistics
#Descriptive statistics are brief descriptive coefficients that
#summarize a given data set, which can be either a representation
#of the entire or a sample of a population.

import pandas as pd
#Create a Dictionary of series
d = {'Age':pd.Series([25,26,25,23,30,29,23,34,40,30,51,46]),
'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,4.10,3.65])}
#Create a DataFrame
df = pd.DataFrame(d)
print(df)
print('############ Sum ########## ')
print (df.sum())
print('############ Mean ########## ')
print (df.mean())
print('############ Standard Deviation ########## ')
print (df.std())
print('############ Descriptive Statistics ########## ')
print (df.describe())
