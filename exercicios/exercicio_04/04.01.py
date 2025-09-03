# 04.01 Quantos clientes tem vínculo com a Twitch?
# %%
import pandas as pd

df = pd.read_csv("../../data/clientes.csv", sep=";")
df
# %%
filtro = df['FlTwitch'] == 1
qtd_clientes = df['FlTwitch'][filtro].count()
print(f'a quantidade de clientes que tem viculo coma  twitch é: {qtd_clientes}')
# %%
contagem = df['FlTwitch'].value_counts()
contagem[1]
# %%
#Como a coluna tem apenas 0 e 1, a soma resulta no total de clientes com vinculo
clientes_twitch = df['FlTwitch'].sum()
print(f"Quantidade de clientes com vínculo com a Twitch: {clientes_twitch}")
# %%
qtd_clientes = df.query('FlTwitch == 1')['FlTwitch'].count()
print(f'A quantidade de clientes que tem vínculo com a Twitch é: {qtd_clientes}')
# %%
