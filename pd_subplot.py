#匯入模組
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from numpy.random import randn, randint, uniform, sample

#資料匯入
iris = sns.load_dataset('iris')

#單純linePlot
iris.plot(kind='line', subplots=True, sharex=False, layout=(2,2)) #sharex: 是否只在最下面顯示x座標；layout: 行列中各要放幾個圖
plt.tight_layout() #讓圖片間不會相互重疊

#呈現
plt.show()