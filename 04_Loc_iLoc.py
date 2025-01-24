import pandas as pd

#loc = localization
df = pd.read_csv('Pandas/pokemon.csv', index_col=1)
print(df.loc["Bulbasaur"])

#iloc
print(df.iloc[9])

print(df.loc["Squirtle", "Total"])

print(df.iloc[0:4])

print(df.loc[:, ["Type 1", "HP", "Total"]])

print(df.head(1))

print(df.iloc [0,[1,4,3]])




