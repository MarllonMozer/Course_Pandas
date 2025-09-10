#%%
import pandas as pd

df = pd.read_csv("dados_cartao.csv", sep=";")
df.head()
# %%
df["dtTransacao"] = pd.to_datetime(df["dtTransacao"])
df["vlVenda"] = df["vlVenda"].astype(float)
df["vlParcelas"] = df["vlVenda"] / df["qtParcelas"]
df["vlParcelas"] = df["vlParcelas"].round(2)
df
# %%
df["ordemParcela"] = df.apply(lambda row: [i for i in range(row['qtParcelas'])], axis=1)
df_explode = df.explode("ordemParcela")
df_explode
# %%
