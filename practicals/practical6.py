import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

A = [71, 75, 65, 69]
B = [90, 80, 86, 84]
C = [72, 77, 76, 79]

data = A + B + C
school_names = (['School_A'] * len(A)) +  (['School_B'] * len(B)) +  (['School_C'] * len(C))
data = pd.DataFrame({'School': school_names, 'score': data})

sns.catplot( data=data , x='School', y='score', dodge=True, kind='violin', aspect=3)
plt.show()

print(data)

data.groupby('School').mean()

overall_mean = data['score'].mean()
print(overall_mean)

# compute Sum of Squares Total
data['overall_mean'] = overall_mean
ss_total = sum((data['score'] - data['overall_mean'])**2)
print(ss_total, data)

# compute group means
group_means = data.groupby('School').mean()
print(group_means)
group_means = group_means.rename(columns = {'score': 'group_mean'})
print(group_means)

# add group means and overall mean to the original data frame
data = data.merge(group_means, left_on = 'School', right_index = True)
print(data)

# compute Sum of Squares Residual, deviation from group mean ssb
ssb = sum((data['score'] - data['group_mean'])**2)
print(ssb)

ssw = sum((data['overall_mean_x'] - data['group_mean'])**2)
print(ssw)

# compute Mean Square Residual
n_groups = len(set(data['School']))
n_obs = data.shape[0]     # no of observation(inputs)
df= n_obs - n_groups      # degree of freedom by group 

# for m*n matrix df = (m-1) * n , for (4 * 3) matrix df = (4-1) * 3 = 9
print("degree of f -->",df)
ms_residual = ssb / df     
print(ms_residual,n_obs,n_groups)

# compute Mean Square Explained
df_by_group = n_groups - 1        # for 3 groups(A,B,C) df = len of unique(groups) - 1 i.e 3 - 1 = 2
ms_explained = ssw / df_by_group
print(ms_explained, df_by_group)

# compute F-Value
f = ms_explained / ms_residual
print(f)

# compute p-value
import scipy.stats
p_value = scipy.stats.f.cdf(0.01, df, df_by_group)
print(p_value)