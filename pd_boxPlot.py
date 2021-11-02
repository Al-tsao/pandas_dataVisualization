#匯入模組
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from numpy.random import randn, randint, uniform, sample

#資料匯入
iris = sns.load_dataset('iris')
df = iris.drop('species', axis = 1)

#繪圖
df.plot(kind='box', figsize=(10,5), vert = False) #vert: 選擇水平或者垂直呈現

#呈現
plt.show()