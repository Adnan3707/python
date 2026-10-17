import pandas as pd
import numpy as np

my_series = pd.DataFrame(
    [0,1,2,3,4],index=['day 0','day 1','day 2','day 3','day 4']
)

multi_df = pd.DataFrame(
    {
        'temperature': [18, 20, 22, 19, 17],
        'humidity': [65, 60, 55, 70, 75],
    },
    index=['day 0', 'day 1', 'day 2', 'day 3', 'day 4'],
)
print(multi_df.iloc[:,0:2])
print(my_series.iloc[:,0])
print(my_series.iloc[3:5])


# print(my_series.loc['day 3'])
# my_series.index=[0,3,4,5,1]
# print('-------------')
# print(my_series.loc[0:1])