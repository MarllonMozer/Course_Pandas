# %%
import pandas as pd

transacoes = pd.read_csv("../data/transacoes.csv", sep=";")
transacoes.head()
# %%
transacoes.groupby(by=["IdCliente"]).count()
# %%
transacoes.groupby(by=["IdCliente"])["IdTransacao"].count()
# %%
# para retornar um dataframe
transacoes.groupby(by=["IdCliente"])[["IdTransacao"]].count()
# %%
# para retornar um dataframe e resetar o index ou nao usar o idCliente como index
transacoes.groupby(by=["IdCliente"], as_index=False)[["IdTransacao"]].count()
# %%
#quantidade de transações
#total de pontos 
# média de pontos por transação - pontos / transação
summary = (transacoes.groupby(by=["IdCliente"], as_index=False)
                     .agg({"IdTransacao":["count"],
                           "QtdePontos":["sum","mean"]}))
summary
# %%
summary.columns
# %%
# para acessar a coluna mean de QtdePontos
summary["QtdePontos"]["mean"]
# passa a hierarquia como uma tupla
summary[("QtdePontos","mean")]
# %%
# para tirar desse multiindex para um colunas simples 
# voce passa as colunas que voce quer
summary.columns = ["IdCliente", "QtdeTransacoes", "TotalPontos", "MediaPontos"]
summary["TotalPontos"]
# %%
