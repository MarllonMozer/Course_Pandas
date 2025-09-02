 # %% 
import pandas as pd

df_clientes = pd.read_csv("../data/clientes.csv", sep=";")
df_clientes
# %%
# Mostra as 10 primeiras linhas
df_clientes.head(10)
# %%
# Mostra as 10 últimas linhas
df_clientes.tail(10)
# %%
# Mostra 10 linhas aleatórias
df_clientes.sample(10)
# %%
# Mostra o número de linhas e colunas
df_clientes.shape
# %%
# Mostra os nomes das colunas
df_clientes.columns
# %%
# Mostra o índice do DataFrame
df_clientes.index
# %%
# Mostra o tipo de dados de cada coluna
df_clientes.info()
# %%
# Mostra o uso de memória do DataFrame valor real
df_clientes.info(memory_usage="deep")

# %%
df_clientes.dtypes
# %%
