# %%
import pandas as pd
idades = [ 18, 26, 19, 21, 37, 23, 25, 24, 22, 54, 18, 44, 19, 21, 25, 23, 22, 43, 21, 41]

series_idades = pd.Series(idades)
series_idades

#%%
idades[0]
# %%
series_idades[-1]
# %%
series_idades = series_idades.sort_values()
series_idades
# %%
series_idades[0]
# %%
series_idades.iloc[3]
# %%
series_idades.iloc[-1]
# %%
series_idades.iloc[:3]
# %%
indexs = ['Ana', 'Beto', 'Cecília', 'Davi', 'Eduardo',
          'Fernanda', 'Gustavo', 'Heloísa', 'Igor', 'Joana',
          'Karla', 'Luiz', 'Mariana', 'Natan', 'Olga',
          'Paulo', 'Quiteria', 'Rafael', 'Sofia', 'Tiago'
          ]
series_idades = pd.Series(idades, index=indexs)
series_idades
# %%
series_idades['Natan']
# %%
series_idades.iloc[2]
# %%
series_idades.iloc[[-1]]
# %%