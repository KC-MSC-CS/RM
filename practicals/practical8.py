# correlation
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 
from scipy.stats import pearsonr, spearmanr

df = pd.read_csv("../Datasets/Admission_Predict.csv")
gre_scores = list(df['GRE Score'])
chance_of_admit = list(df['Chance of Admit '])

print("GRE Scores - mean: ",np.mean(gre_scores)," std-dev: ",np.std(gre_scores))
print("Chance of Admission - mean: ",np.mean(chance_of_admit)," std-dev: ",np.std(chance_of_admit))

plt.scatter(gre_scores,chance_of_admit)
plt.show()

# cov(X, Y) = (sum (x - mean(X)) * (y - mean(Y)) ) * 1/(n-1)
covariance = np.cov(gre_scores, chance_of_admit)
print("Covariance matrix: ",covariance)

# Pearson's correlation coefficient = covariance(X, Y) / (stdv(X) * stdv(Y))
pearson_corr,_ = pearsonr(gre_scores, chance_of_admit)
print("Pearson's correlation score: ",pearson_corr)

# Spearman's correlation coefficient = covariance(rank(X), rank(Y)) / (stdv(rank(X)) * stdv(rank(Y)))
spearman_corr,_ = spearmanr(gre_scores, chance_of_admit)
print("Spearman's correlation score: ",spearman_corr)
