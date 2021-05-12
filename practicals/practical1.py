import requests
import urllib
import pandas as pd

# Read a csv file
# df = pd.read_csv("../Datasets/churn_modelling.csv")
# print(df.iloc[:5,:5])

# url = "http://winterolympicsmedals.com/medals.csv"
# data = requests.get(url)
# print(data)

# with open('medals.csv', 'r') as f:
#     f.write(data.text)

df2 = pd.read_csv('medals.csv')
print(df2.head())



