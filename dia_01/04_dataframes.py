# %%
import pandas as pd
idades = [ 
          18, 26, 19, 21, 41,
          37, 23, 25, 24, 22,
          54, 18, 44, 19, 21,
          25, 23, 22, 43, 21 
        ]

nomes = ['Ana', 'Beto', 'Cecília', 'Davi', 'Eduardo',
          'Fernanda', 'Gustavo', 'Heloísa', 'Igor', 'Joana',
          'Karla', 'Luiz', 'Mariana', 'Natan', 'Olga',
          'Paulo', 'Quiteria', 'Rafael', 'Sofia', 'Tiago'
          ]

series_idades = pd.Series(idades)
series_nomes = pd.Series(nomes)
# %%
df = pd.DataFrame()
df['idades'] = series_idades
df['nomes'] = series_nomes
df
# %%
type(df)
# %%
type(series_idades)
# %%
df['nomes']
# %%
df.iloc[0]
# %%
# Acessa a primeira linha da coluna nomes
df.iloc[0]['nomes']
# %%
# Acessa a última linha da coluna idades
df.iloc[-1]["idades"]
# %%
# Acessa a última linha
df.iloc[-1]
# %%
