# %%
from calendar import c
import re
import pandas as pd
from sqlalchemy import column
df = pd.read_csv("../data/transacoes.csv", sep=";")
df
# %%
df.shape
# %%
df.info(memory_usage="deep")
# %%
df.dtypes
# %%
# Pode renomear as colunas das 2 formas abaixo
df = df.rename(columns={
                        "QtdePontos" : "qtPontos",
                        "DescSistemaOrigem" : "SistemaOrigem"
                        })
# %%
renamed_columns = {
                  "QtdePontos" : "qtPontos",
                  "DescSistemaOrigem" : "SistemaOrigem"
                 }  
df = df.rename(columns=renamed_columns)
df
# %%
renamed_columns = {
                  "QtdePontos" : "qtPontos",
                  "DescSistemaOrigem" : "SistemaOrigem"
                 } 
# se eu colocar inplace=True, ele altera o df original sem precisar fazer df = df.rename(atribuir)
df.rename(columns= renamed_columns, inplace=True)
df
# %%
# Passa uma lista com os nomes das colunas que quer selecionar
df[["IdCliente", "qtPontos"]] 
colunas = ["IdCliente", "qtPontos"]
df[colunas]
# %%
#comparar com o SQL
# SELECT * FROM df
df
# SELECT IdCliente FROM df
df[["IdCliente"]]
# SELECT IdCliente, qtPontos FROM df LIMIT 5
df[["IdCliente", "qtPontos"]].head(5) # Poderia ser sample(5) ou tail(5)
# %%
# SELECT idCliente, idTransacao, qtPontos FROM df LIMIT 5
df[["IdCliente", "IdTransacao", "qtPontos"]].head(5)
# %%
# Para ordenar seu dataset 
colunas = df.columns.tolist()
colunas.sort()
colunas

df = df[colunas]
df
# %%
