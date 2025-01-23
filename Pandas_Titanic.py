#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#import data from Kaggle > Titanic > Train.csv


# In[1]:


import pandas as pd
import numpy as np


# In[78]:


df= pd.read_csv("train.csv")
print(df)


# In[80]:


df.shape


# In[82]:


df.head() #first 5 line


# In[84]:


df.tail() #last 5 line


# In[86]:


df['Survived'] #series


# In[88]:


df[['Name', 'Survived']]


# In[90]:


df.iloc[0]


# In[92]:


df.iloc[0:2]


# In[94]:


df.iloc[-1]


# In[96]:


df.loc[0, "Name"]


# In[114]:


df.loc[0:4, "Name"]


# In[35]:


df.describe()


# In[100]:


df.dtypes


# In[41]:


df.isnull()


# In[102]:


df.isnull().sum()


# In[ ]:


df.drop('Cabin', axis = 1, inplace=True)


# In[108]:


df.head()


# In[118]:


df= pd.read_csv("train.csv")
print(df)


# In[122]:


df.corr(numeric_only=True)


# In[130]:


import matplotlib.pyplot as plt
import seaborn as sns


# In[132]:


corr = df.corr(numeric_only=True)
fig, ax = plt.subplots(figsize=(16, 6))
sns.heatmap(
    corr,
    vmin=-1, vmax=1, center=0, annot=True,
    cmap=sns.diverging_palette(20, 220, n=200),
    square=True
)
plt.show()


# In[134]:


#data analysis for pattern


# In[ ]:


#quanti biglietti venduti?


# In[148]:


pclass_df = df.groupby("Pclass").count() ["PassengerId"].to_frame(name= "Biglietti Venduti")
pclass_df


# In[144]:


pclass_df.plot(kind="bar")


# In[156]:


#quante persone sono sopravvisute per classe?


# In[162]:


df_survived = df [["Pclass", "Survived"]].groupby('Pclass').mean()
df_survived


# In[166]:


df_survived.plot(kind='bar')


# In[168]:


df_survived_2 = df [["Pclass", "Survived"]].groupby('Pclass').mean().reset_index()
df_survived_2 #se voglio fare il reset


# In[170]:


#sesso persone / sopravvivenza


# In[174]:


df[['Survived', 'Sex']].groupby('Sex').mean().plot(kind='bar')


# In[176]:


df[['Survived', 'Sex']].groupby('Sex').mean()


# In[178]:


# contare per sesso i sopravvissuti


# In[182]:


survivors_df = df[['Survived', 'Sex']].groupby('Sex').sum()
survivors_df["Total"] = df[['Survived', 'Sex']].groupby('Sex').count()
survivors_df.plot(kind= 'bar')


# In[186]:


survivors_df['%'] = (survivors_df['Survived']*100)/survivors_df['Total']
survivors_df


# In[188]:


#età vs sopravvivenza


# In[190]:


children_df = df [df['Age'] <= 17]
children_df.head()


# In[203]:


total_children = children_df.shape[0] #numero di righe
total_children


# In[207]:


children_survived = children_df['Survived'].sum()
children_survived


# In[213]:


adults_df = df[df['Age']>17]
adults_df = adults_df.rename(columns= {'Sex' : 'People'})
adults_df


# In[217]:


adults_df = df[df['Age'] > 17]  # Filtra i dati per età maggiore di 17
adults_df = adults_df.rename(columns={'Sex': 'People'})  # Rinomina la colonna 'Sex' in 'People'

# Raggruppa per 'People' e somma la colonna 'Survived'
survivors_df = adults_df[['Survived', 'People']].groupby('People').sum()
# Conta il numero totale di persone per ciascun gruppo ('People')
survivors_df['Total'] = adults_df[['Survived', 'People']].groupby('People').count()['Survived']
# Calcola la percentuale di sopravvissuti
survivors_df['%'] = (survivors_df['Survived'] * 100 / survivors_df['Total'])
# Mostra il risultato
survivors_df


# In[219]:


survivors_df.loc['children'] = [children_survived, total_children, (children_survived*100)/total_children]
survivors_df


# In[225]:


survivors_df [['Survived', 'Total']].plot(kind='bar')


# In[227]:


# analisi per famiglie


# In[232]:


#sopravvivenza medi per num famiglia


# In[240]:


# Assicurati che le colonne siano numeriche e senza NaN
df['SibSp'] = pd.to_numeric(df['SibSp'], errors='coerce').fillna(0)
df['Parch'] = pd.to_numeric(df['Parch'], errors='coerce').fillna(0)
df['Survived'] = pd.to_numeric(df['Survived'], errors='coerce').fillna(0)

# Calcola la dimensione della famiglia
df['family_size'] = 1 + df['SibSp'] + df['Parch']

# Raggruppa e calcola la media della sopravvivenza per dimensione della famiglia
survival_rates = df.groupby('family_size')['Survived'].mean()

# Visualizza i risultati in un grafico a barre
survival_rates.plot(kind='bar', figsize=(10, 6))

# Migliora il grafico
import matplotlib.pyplot as plt
plt.title('Percentuale media di sopravvivenza in base alla dimensione della famiglia')
plt.xlabel('Dimensione della famiglia')
plt.ylabel('Percentuale di sopravvivenza media')
plt.xticks(rotation=0)  # Mantieni le etichette leggibili
plt.show()


# In[242]:


df.head()


# In[246]:


df['Title'] = df['Name'].apply(lambda x: x.split(',')[1].split('.')[0].strip())
df


# In[250]:


df.groupby('Title').count()['PassengerId'].sort_values().plot(kind='bar', logy=True)


# In[ ]:


#sopravvisuti per titolo


# In[273]:


# Calcola la media dei sopravvissuti per ogni titolo
grouped = df.groupby('Title')['Survived'].mean()

# Controlla il risultato prima di fare il plot
print(grouped)

# Riprova a fare il plot
grouped.sort_values().plot(kind='bar')


# In[279]:


# Raggruppa per 'Title' e conta i valori nella colonna 'PassengerId'
df.groupby('Title').count()[['PassengerId']]


# In[ ]:




