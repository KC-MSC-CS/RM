# Multiple linear regression 
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
from mpl_toolkits import mplot3d
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

df = pd.read_csv("../Datasets/Admission_Predict.csv")
df = df.drop('Serial No.',axis=1)

print(df.head())

x = df['GRE Score']
y = df['Chance of Admit ']
z = df['TOEFL Score']

print(x.head())
print(y.head())
print(z.head())

# Creating figure
fig = plt.figure(figsize = (10, 7))
ax = plt.axes(projection ="3d")
ax.scatter3D(x, y, z, color = "green")
ax.set_xlabel('GRE Score', fontweight ='bold') 
ax.set_ylabel('Chance of Admission', fontweight ='bold') 
ax.set_zlabel('TOEFL Score', fontweight ='bold')
plt.title("simple 3D scatter plot")
plt.show()

x = df.iloc[:,:-1]
y = df.iloc[:,-1]

x_train,x_test,y_train,y_test = train_test_split(x,y)

model = LinearRegression()
model.fit(x_train,y_train)
score = model.score(x_test,y_test)

print("Model score: ",score)

y_pred = model.predict(x_test)
score = r2_score(y_test,y_pred)

print("R2 score: ",score)

