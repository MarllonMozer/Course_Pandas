# Quantos clientes tem um saldo de pontos maior que 1000?
# %%
import pandas as pd

df = pd.read_csv("../../data/clientes.csv", sep=";")
df
# %%
filtro = df["QtdePontos"] > 1000
result = df["QtdePontos"][filtro].count()
print(f"a quantidade de clientes com mais de 1000 pontos é: {result}")
# %%
df.columns
# %%
