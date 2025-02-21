# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 13:31:00 2025

@author: grantajo
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pearsonr
import seaborn as sns

#%%

df = pd.read_csv('C:/Users/grantajo/Box/1 Research/Code Repository/Data Analysis/Gleeble_Data.csv')

df_edit = df.drop(columns=['Sample'])

cor = np.corrcoef(df_edit, rowvar=False)
cor

im = plt.imshow(cor, vmin=-1, vmax=1, cmap='coolwarm')
plt.colorbar(im)
plt.show()

pearson_corr = df_edit.corr(method='pearson')

r_value, p_value = pearsonr(df_edit['Hardness'],df_edit['Perimeter Fraction - Austenite'])
r_value1, p_value1 = pearsonr(df_edit['Hardness'],df_edit['Area Fraction (%) - Ferrite'])

ax = sns.heatmap(
    pearson_corr, 
    annot=True, 
    cmap='coolwarm', 
    fmt='.2f', 
    linewidths=0.5,
    annot_kws={"size":5}
    )
plt.title('Pearson Correlation Matrix Heatmap')
plt.xticks(fontsize=8)
ax.set_yticks(range(len(pearson_corr)))
ax.set_yticklabels(pearson_corr.index, rotation=0, fontsize=8)
plt.show()

kendall_corr = df_edit.corr(method='kendall')
ax1 = sns.heatmap(
    kendall_corr,
    annot=True,
    cmap='coolwarm',
    fmt='.2f',
    linewidths=0.5,
    annot_kws={"size":5}
    )
plt.title('Kendall Correlation Matrix Heatmap')
plt.xticks(fontsize=8)
ax1.set_yticks(range(len(pearson_corr)))
ax1.set_yticklabels(pearson_corr.index, rotation=0, fontsize=8)
plt.show()

spearman_corr = df_edit.corr(method='spearman')
ax2 = sns.heatmap(
    spearman_corr,
    annot=True,
    cmap='coolwarm',
    fmt='.2f',
    linewidths=0.5,
    annot_kws={"size":5}
    )
plt.title('Spearman Correlation Matrix Heatmap')
plt.xticks(fontsize=8)
ax2.set_yticks(range(len(pearson_corr)))
ax2.set_yticklabels(pearson_corr.index, rotation=0, fontsize=8)
plt.show()
