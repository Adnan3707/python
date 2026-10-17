import pandas as pd
import numpy as np

my_data = pd.DataFrame(
    [0,1,2,3,4],index=['day 0','day 1','day 2','day 3','day 4']
)

print(my_data[0])
# print(my_series.loc[my_series[0] > 2])

my_series = pd.Series([0,1,2,3,4],index=['day 0','day 1','day 2','day 3','day 4'])

print(my_series == 2)
print('---------')

# filter
print(my_series.loc[my_series == 2])
print(my_series.loc[-my_series.isin([1,3])])
print(my_series.loc[my_series>3])