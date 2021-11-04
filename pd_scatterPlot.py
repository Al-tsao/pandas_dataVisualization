#匯入模組
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from numpy.random import randn, randint, uniform, sample

#資料匯入
iris = sns.load_dataset('iris')
df = iris.drop('species', axis = 1)

#繪圖-單純散佈圖
df.plot(kind='scatter', x = 'sepal_width', y = 'petal_width')

#繪圖-配合密度
df.plot(kind='scatter', x = 'sepal_width', y = 'petal_width', c = 'sepal_length')

#呈現
plt.show()