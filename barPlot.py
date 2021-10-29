import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from numpy.random import randn, randint, uniform, sample

#資料匯入
iris = sns.load_dataset('iris')

df = iris.drop(['species'], axis = 1)

#單純bar plot
df.plot(kind = 'bar')
plt.show()




