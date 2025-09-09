# 06.02 - Quais são os usuários que mais fizeram transações? 
# Considere os 10 primeiros.
# %%
import pandas as pd

transacao = pd.read_csv("../../data/transacoes.csv", sep=";")

transacao.head()
# %%
(transacao.groupby(by=["IdCliente"])["IdTransacao"]
           .count()
           .sort_values(ascending=False)
           .head(10))
# %%
