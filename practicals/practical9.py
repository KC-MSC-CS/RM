# Simple Linear Regression 
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df = pd.read_csv("Datasets/Admission_Predict.csv")
gre_scores = df['GRE Score']
chance_of_admit = df['Chance of Admit ']

x = gre_scores
y = chance_of_admit

x = np.array(gre_scores).reshape(-1,1)
y = np.array(chance_of_admit).reshape(-1,1)

print(x)
print(y)

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.25)

model = LinearRegression()
model.fit(x_train,y_train)
score = model.score(x_test,y_test)
print("Model score: ",score)

y_pred = model.predict(x_test)

plt.scatter(x_test,y_test, color='b')
plt.plot(x_test,y_pred,color='k')
plt.show()