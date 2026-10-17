import numpy as np
rng = np.random.default_rng(616)
inventory = rng.integers(0,100,10)

price = rng.random(10).round(2)
print((price*inventory).sum())