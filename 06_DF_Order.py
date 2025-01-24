import pandas as pd

df = pd.read_csv("Pandas/pokemon.csv") 

sdf = df.sort_index()
print(sdf.head(3))

sdf = df.sort_index(ascending= False)
print(sdf.head(3))

sdf = df.sort_values(by= "Name", ascending=False)
print(sdf.head(3))

sdf = df.sort_values(by= ["Total", "HP"])
print(sdf.head(5))

print(sdf[["Name", "Total", "HP"]].head(5))

sdf = df.sort_values(by= ["Total", "HP"], ascending=[False, True])
print(sdf[["Name", "Total", "HP"]].head(10))