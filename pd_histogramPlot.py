#匯入模組
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from numpy.random import randn, randint, uniform, sample

#資料匯入
iris = sns.load_dataset('iris')

#垂直
iris.plot(kind='hist', bins=30, stacked=True) #bins: 要分幾組；stacked: 是否要堆疊

#水平
iris.plot(kind='hist', bins=30, stacked=True, orientation='horizontal')

#多小圖
df = iris.drop('species', axis = 1)
df.hist(color = 'r', alpha = 0.5) #color: 直方圖顏色；alpha: 調整透明度

#呈現
plt.show()