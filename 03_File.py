import pandas as pd
import numpy as np

df = pd.read_csv('Pandas/pokemon.csv')
#print(df)

# #if csv is tabuleted and not with ,
# df = pd.read_csv('Pandas/pokemon.csv', sep = '\t', delimiter='')
# print(df)

# # df1 = pd.read_json('Pandas/pokemon.json')
# # print(df1)

# # df2 = pd.read_excel('Pandas/pokemon.xlsx', index_col=0)
# # print(df2)


#Read data from df
df = pd.read_csv('Pandas/pokemon.csv')
print(df[0:2]) #slicing

print(df["Name"][0:4]) #for column

print(df[["Name", "Defense", "HP", "Sp. Atk", "Sp. Def"]].head(10))

print(df.iloc[0,1]) #loc = localization, index and column