import pandas as pd

df = pd.read_csv("Pandas\pokemon.csv")

df ["Will"] = "Ciao"
print(df)
print(df[["Name", "Total", "Will"]])

df[["Will", "Switch", "Gameboy"]] = ["2nd", "7th", "1st"]
print(df[["Name", "Total","Will","Switch", "Gameboy"]])

df1 = pd.read_csv("Pandas\pokemon.csv")
df1.insert(1, "Nome", "Frank")
print(df1)

df1 = df1.assign(Will = "querty")
print(df1)

print(">>>>>>>>>>>REMOVE COLUMS")
df.drop("Legendary", inplace= True, axis= 1)
print(df)

colPop = df.pop("Name") #save the removed column
print(df.head(2))
print(colPop.head(2))

print(df.iloc[:,[1,2,3,5,4,2]])

columns= list(df.columns)
columns.reverse()
print(df[columns])

columns = df.columns.tolist()
columns.reverse()
df = df[columns]
print(df)