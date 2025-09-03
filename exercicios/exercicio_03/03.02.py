# %%
import pandas as pd

df = pd.read_csv("../../data/transacoes.csv", sep=";")
df
# %%
qtd_colunas_int = df.select_dtypes(include="int64").shape[1]
print(f"tem {qtd_colunas_int} coluna inteira no arquivo transacoes.csv")
# %%
