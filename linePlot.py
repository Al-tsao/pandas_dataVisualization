import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from numpy.random import randn, randint, uniform, sample

# df = pd.DataFrame(randn(1000), index = pd.date_range('2021-10-25', periods=1000), columns=['values'])
# ts = pd.Series(randn(1000), index = pd.date_range('2021-10-25', periods=1000))
# df['values'] = df['values'].cumsum()
# ts = ts.cumsum()
# sns.set()   
# ts.plot()
# df.plot()
# plt.show()

#資料匯入
iris = sns.load_dataset('iris')

#單純linePlot
iris.plot(kind='line', figsize=(10, 5)) #kind選擇想要圖形；figsize調整圖形大小
plt.show()

#雙座標linePlot
mainYaxis = pd.DataFrame(iris, columns=['sepal_length', 'petal_length'])
minorYaxis = pd.DataFrame(iris, columns=['sepal_width', 'petal_width'])
main = mainYaxis.plot()
minorYaxis.plot(kind='line', figsize=(16, 10), secondary_y = True, ax=main)
#ax: matplotlib axes object 到底甚麼是axes? => https://towardsdatascience.com/what-are-the-plt-and-ax-in-matplotlib-exactly-d2cf4bf164a9
plt.show()





