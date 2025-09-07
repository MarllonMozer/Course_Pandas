# %%
import pandas as pd
from prometheus_client import Summary

transacoes = pd.read_csv("../data/transacoes.csv", sep=";")
transacoes.head()
# %% 
transacoes["DtCriacao"] = transacoes["DtCriacao"].str[:10]
# %%
# calcular a amplitude e calcular a distanca da amplitude para media elevado ao quadrado
# sqrt((amplitude - media) **2)
import numpy as np

def diff_amp(x: pd.Series):
   amplitude = x.max() - x.min()
   media = x.mean()
   return np.sqrt((amplitude - media) **2)

def life_time(x: pd.Series):
    dt = pd.to_datetime(x)
    return (dt.max() - dt.min()).days
# %%
idades = pd.Series([22, 35, 46, 27, 19, 30, 41, 18, 23, 50, 33, 26, 39, 28, 31, 77])
idades.mean()
diff_amp(idades)
# %%
summary = (transacoes.groupby(by=["IdCliente"], as_index=False)
          .agg({
              "IdTransacao":["count"],
              "QtdePontos":["sum","mean", diff_amp],
              "DtCriacao":[life_time]}))

# %%
summary.columns
# %%
summary.columns = ["IdCliente",
                   "QtdeTransacoes",
                   "TotalPontos",
                   "MediaPontos",
                   "DiffAmpPontos",
                   "LifeTime"]
summary
# %%
