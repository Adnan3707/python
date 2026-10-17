import pandas as pd
import numpy as np

arra = np.arange(5)
series = pd.Series(arra)
print(series.values)
print(series.values.mean())
series.index=[10,20,30,40,50]
print(series)

arr1 = np.random.random(100)
oil_series = pd.Series(arr1,name='oil series')
print(oil_series)