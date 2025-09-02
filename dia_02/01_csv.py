# %%
import pandas as pd


series = pd.Series([1, 2, 3, 4, 5])
series
# %%
df = pd.read_csv("../data/clientes.csv")
df

# %%
df.to_csv("clientes_novo.csv", index=False)
# %%
df.to_parquet("clientes_novo.parquet", index=False)
# %%
df_2 = pd.read_parquet("clientes_novo.parquet")
df_2
# %%
df.to_excel("clientes_novo.xlsx", index=False)
# %%
df_3 = pd.read_excel("clientes_novo.xlsx")
df_3
# %%
df_bobo = pd.read_csv("../data/bobo.csv", sep=";")
df_bobo
# %%
