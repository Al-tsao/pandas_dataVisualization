#匯入模組
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from numpy.random import randn, randint, uniform, sample

#資料匯入
iris = sns.load_dataset('iris')
df = iris.drop(['species'], axis = 1)

#單純pie plot
df.iloc[0].plot(kind='pie')

#單純pie plot
df_sub = df.head(3).T #T: 轉置索引和列
df_sub.plot(kind='pie', legend=False, subplots=True, fontsize= 10, autopct='%.2f', figsize=(20,20))

#呈現
plt.show()