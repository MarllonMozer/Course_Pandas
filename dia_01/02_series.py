#%%
idades = [ 18, 26, 19, 21, 37, 23, 25, 24, 22, 54, 18, 44, 19, 21, 25, 23, 22, 43, 21, 41]

media = sum(idades) / len(idades)
print("media:",media)

diffs = 0
for i in idades:
    diffs += (i - media) ** 2
    
variancias = diffs / (len(idades)-1)
print("variancias:",variancias)

from re import S
import pandas as pd

series_idades = pd.Series(idades)
series_idades


# %%
# Estatisticas da Series
media_series = series_idades.mean()  # Calcula a média
variancia_series = series_idades.var()   # Calcula a variância
summary_idades = series_idades.describe()  # Resumo estatístico
summary_idades

# %%
