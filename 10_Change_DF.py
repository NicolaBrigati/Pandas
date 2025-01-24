import pandas as pd

# with loc and iloc you can select data
#filterd data
# to delate use drop or fillna
#remove duplicate df.duplicated

df = pd.read_csv("Pandas\pokemon.csv")

df.loc[df['Name'] == 'Bulbasaur', 'Name'] = 'Babasaur'
print(df.head(1))

df.loc[df['Name'] == 'Babasaur', ['Type 1', 'Type 2']] = 'Querty'
print(df.head(1))

df.loc[df['Name'] == 'Babasaur', ['Type 1', 'Type 2']] = ['Grass', 'Poison']
print(df.head(1))

df.loc[(df['Name'].str.contains('saur')) & (df['Total'] > 500), ['Type 1', 'Type 2']] = ['Query', 'Querty']
print(df.head(4))

df.loc[(df['Name'].str.contains('saur')), 'Type 1'] = 'Query'
print(df.head(4))