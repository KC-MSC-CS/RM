import matplotlib.pyplot as plt 
import pandas as pd 
import numpy as np 

df = pd.read_csv("../Datasets/churn_modelling.csv")
print(df.head())
total_countries = df['Geography'].value_counts().count()
print(df['Geography'].value_counts())

# HISTOGRAM PLOT 
plt.hist(df['Geography'],facecolor='coral',edgecolor='blue',bins=total_countries)

# PIE CHART 
# all rows with age greater than 40 and less than 50 
age_lt_50 = df[df['Age'] > 40]
age_lt_50 = age_lt_50[age_lt_50['Age'] < 50]['Age']   # Take only the age column
# all rows with age less than 40
age_lt_40 = df[df['Age'] < 40]['Age']                 # Take only the age column
# all rows with age greater than or equal to 50
age_gt_50 = df[df['Age'] >= 50]['Age']                # Take only the age column
labels = ['greater than 40 but less than 50','less than 40','greater than or equal to 50']
values= [age_lt_50.value_counts().count(),age_lt_40.value_counts().count(),age_gt_50.value_counts().count()]
print(values)
plt.pie(values,labels=labels)
plt.axis('equal')
plt.show()

# LINE CHART 
df2 = pd.read_csv("Datasets/stock_prices.csv")
df2['Date'] = pd.to_datetime(df2['Date'])
fig = plt.figure(figsize=(10,6))
ax1 = fig.add_axes([0,0,1,1])    # [left,bottom,width,height]
ax2 = fig.add_axes([])
ax1.set_title("Tesla stock prices")
ax1.plot(df2['Date'],df2['Close'],color='green')
plt.show()
# Line plot with subplots 
fig,axes =  plt.subplots(2,2,figsize=(15,10))
axes[0][0].plot(df2['Date'],df2['Close'],color='green')
axes[0][0].set_title('stock price 1')
axes[0][1].plot(df2['Date'],df2['Close'],color='blue')
axes[0][1].set_title('stock price 2')
axes[1][0].plot(df2['Date'],df2['Close'],color='coral')
axes[1][0].set_title('stock price 3')
axes[1][1].plot(df2['Date'],df2['Close'],color='yellow')
axes[1][1].set_title('stock price 4')
plt.show()

# Box plot 
f = plt.figure(figsize=(10,5))
ax = f.add_axes([0,0,1,1])
bp = ax.boxplot(df['CreditScore'],notch=True,patch_artist=True)
bp['boxes'][0].set(facecolor='blue')
plt.title("Customer credit scores")
plt.show()

# Violin plot 
f = plt.figure(figsize=(10,10))
ax = f.add_axes([0,0,1,1])
data = [df['CreditScore'],df['CreditScore'],df['CreditScore']]
vp = ax.violinplot(data,showmedians=True)
vp['bodies'][0].set(facecolor='blue')
vp['bodies'][1].set(facecolor='green')
vp['bodies'][2].set(facecolor='coral')
plt.title("Customer credit scores")
plt.show()

# BAR PLOT 
males = df[df['Gender'] == 'Male'].value_counts().count()
females = df[df['Gender'] == 'Female'].value_counts().count()
values = [males,females]
labels = ['male','female']
fig = plt.figure(figsize=(10,6))
ax = fig.add_axes([0,0,1,1])
ax.bar(labels,values)
plt.show()

# SCATTER PLOT 
fig = plt.figure(figsize=(10,6))
ax = fig.add_axes([0,0,1,1])
ax.scatter(df3['CGPA'],df3['Chance of Admit '])
plt.title("CGPA vs chance of getting admission")
plt.xlabel('CGPA')
plt.ylabel("Chance of getting admission")
plt.show()