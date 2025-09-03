# %%
import pandas as pd

df = pd.read_csv("../../data/clientes.csv", sep=";")
qtd_pts = df.iloc[9]['QtdePontos']
print(f"a quantidades de pontos do cliente na 10° posiçao é: {qtd_pts}")
# %%
df.head(10)
# %%
