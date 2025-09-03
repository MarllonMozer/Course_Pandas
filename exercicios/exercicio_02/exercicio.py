# %%

import pandas as pd

df = pd.read_csv("../../data/transacoes.csv", sep=";")
df
# %%
df['valores'] = 1
df
# %%
df.to_csv("transaçoes_1.csv", index=False)
print("Arquivo salvo com sucesso como 'transacoes_1.csv'")
print(f"Shape do DataFrame: {df.shape}")
print(f"Colunas: {list(df.columns)}")
# %%
