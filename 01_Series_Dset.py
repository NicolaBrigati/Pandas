# series = array in np in 1D = column
# ds = several columns together


import pandas as pd
import numpy as np

ds = [5, 10, 15, 20 ,25]
ps = pd.Series(ds)
print(ps)

print(ds[0]) #get index

#label
ds = [5, 10, 15, 20 ,25]
ps = pd.Series(ds, index= ["x", "y", "j", "z", "w"])
print(ps)

#series from dict
ds1 = {"x" :5, "y" :10, "j" :15, "z" : 20, "w" :25}
ps = pd.Series(ds1, index = ["x", "z"])
print(ps)
