#匯入模組
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from numpy.random import randn, randint, uniform, sample

#資料匯入
iris = sns.load_dataset('iris')
df = iris.drop('species', axis = 1)


df['test'] = [1]*df.shape[0]
print(df)

#繪圖
df.plot(kind='hexbin', x = 'sepal_length', y = 'petal_length',  gridsize = 15)

#呈現
plt.show()