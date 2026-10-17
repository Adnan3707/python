import pandas as pd
import numpy as np

series = [16,0,77,82,12,11]
items= ['coffee','tea','milk','suger','lemon','juice']

inventory = pd.Series(np.array(series),index=items)
print(inventory['tea'])

series1 = [16,0,77,82,12,11]
items1 = ['coffee','coffee','milk','suger','lemon','juice']
inventory1 = pd.Series(np.array(series1),index=items1)
print(inventory1['coffee'])

print(inventory1.reset_index(drop=True).iloc[0])