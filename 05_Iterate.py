#iterate items = key:value
#iter rows = index:Row
#iter tuples

import pandas as pd

df = pd.read_csv('Pandas/pokemon.csv').head(1)

for key,value in df.items():
    print(key)

print(">>>>>>>>Iter Rows")
for index,row in df.iterrows():
    print(index, row)

print(">>>>>>>>>>>>>>>>>>ter tuple)")
for row in df.itertuples():
    print(row)

for index, row in df.iterrows():
    if(index==0):
        row['Name'] = 'Blubasaura'
        print(row)
print(df.head(1))
