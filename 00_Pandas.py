#Numpy + Pandas
#in "extension" go to Excel viewer and Install it

import pandas as pd
import numpy as np

ds = {
    "Mesi": ["Gennaio", "Febbraio", "Marzo", "Aprile", "Maggio", "Giugno", "Luglio", "Agosto", "Settembre", "Ottobre", "Novembre", "Dicembre"],
    "Giorni": [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  # Giorni di ogni mese in ordine
}

df = pd.DataFrame(ds)
print(df)

