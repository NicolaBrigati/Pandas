import pandas as pd

df = pd.read_csv("Pandas\pokemon.csv")

df2 = df[["#", "Name", "Total"]]
print(df2)

#create csv
df2.to_csv("Pandas\mini_pkemon.csv", index = False)

#compressed csv
# compressed_df2 = dict(method = 'zip', archive_name = 'nuovi_pokemon.csv')
# df2.to_csv('nuovi_pokemon.zip', index = False, compression = compressed_df2)

#rename sheet
df2.to_excel(r"Pandas\nuovi_pokemon.xlsx", index = False, sheet_name = "pokemon_totali")

#from 3 differents df to 1 file
df3 = df[["#", "Name", "Total"]]
df4 = df[["#", "Name", "HP", "Sp. Atk"]]
df5 = df[["#", "Name", "Attack", "Sp. Atk", "Speed", "Generation"]]

with pd.ExcelWriter(r"Pandas\nuovi_pokem.xlsx") as writer:
    df3.to_excel(writer, sheet_name = "Totali", index = False)
    df4.to_excel(writer, sheet_name = "Stats", index = False)
    df5.to_excel(writer, sheet_name = "Querty", index = False)

#change df
df6 = df.iloc[0:10, 0:4]
#append sheet to nuovi pokemon file
with pd.ExcelWriter(r"Pandas\nuovi_pokem.xlsx", mode = 'a') as writer:
    df6.to_excel(writer, sheet_name="foglio_appeso")