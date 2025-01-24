import pandas as pd

ds = {
    "Mesi": ["Gennaio", "Febbraio", "Marzo", "Aprile", "Maggio", "Giugno", "Luglio", "Agosto", "Settembre", "Ottobre", "Novembre", "Dicembre"],
    "Giorni": [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  # Giorni di ogni mese in ordine
}
df = pd.DataFrame(ds)
print(df)


ds1 = {
    "Mesi": ["Gennaio", "Febbraio", "Marzo", "Aprile", "Maggio", "Giugno", "Luglio", "Agosto", "Settembre", "Ottobre", "Novembre", "Dicembre"],
    "Giorni": [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
    "Stagione" : ["Inverno", "Inverno", "Primavera", "Primavera", "Primavera", "Estate", "Estate", "Estate", "Autunno", "Autunno", "Autunno", "Inverno" ], 
    "Festivita": [ "Capodanno",  "Carnevale",   "Festa del Papà",   "Pasqua", "Pasquetta", "Festa dei Lavoratori", "Festa della Repubblica", "Ferragosto",  "Ognissanti",  "Immacolata Concezione", "Morti",  "Natale" ]
}

df1 = pd.DataFrame(ds1)
print(df1)

print(df1.loc[0])

print(df1.loc[[0,1]]) #list of index for indexing

