# 04.03 - Quantas transações ocorreram no dia 2025-02-01?
# %%
import pandas as pd 

df = pd.read_csv("../../data/transacoes.csv", sep=';')
df
# %%
df.columns
# %%
df["data_nova"] = df["DtCriacao"].str[:10]
filtro = df["data_nova"] == "2025-02-01"
result = df["data_nova"][filtro].count()
print(f"ocorreram no dia 2025-02-01, {result} transaçoes")
