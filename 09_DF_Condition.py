import pandas as pd

# with loc and iloc you can select data
#filterd data

df = pd.read_csv("Pandas\pokemon.csv")
#conditions
print(df[df.Name == 'Bulbasaur'])

print(df[df['Name'].str.contains('saur')])

filtro = ['Bulbasaur', 'Charmander', 'Squirtle']
print(df[df['Name'].isin(filtro)])

print(df[df['Total']>700])

print(df[(df['Total']>700) & (df["Sp. Atk"] > 160)])

print(df[(df['Total']>760) | (df["Sp. Atk"] < 250)])

print(df.loc[(df.Name == 'Bulbasaur'), ['Name', 'HP', 'Generation']])

print(df.loc[(df.Name.str.contains ('Bulbasaur')), ['Name', 'HP', 'Generation']])

print(df.query('Name == "Bulbasaur"'))

print(df.query('Total > 750 and Speed > 100'))