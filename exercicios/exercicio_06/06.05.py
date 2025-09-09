# Qual a média de transações / dia?
# %%
import pandas as pd

transacoes = pd.read_csv("../../data/transacoes.csv", sep=";")
transacoes.head()
# %%
transacoes["DtCriacao"] = transacoes["DtCriacao"].str[:10]
transacoes.head()
# %%
transacoes["dtDia"] = pd.to_datetime(transacoes["DtCriacao"]).dt.date

summary = transacoes.agg({
    "IdTransacao": "count",
    "dtDia": "nunique"
})
transacoes_dia = summary["IdTransacao"] / summary["dtDia"]
transacoes_dia
# %%
