import numpy as np
#匯入模組
import pandas as pd
import matplotlib.pyplot as plt
from pandas.core.reshape.reshape import stack
import seaborn as sns
from numpy.random import randn, randint, uniform, sample

df=pd.DataFrame(randn(10, 4), columns=['a','b','c','d'])

#直條堆疊圖
df.plot(kind='barh', stacked=True)

#橫條堆疊圖
df.plot(kind='barh', stacked=True)

#呈現
plt.show()