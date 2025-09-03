# %%
import pandas as pd

df = pd.read_csv("../../data/clientes.csv", sep=";")

#id_cliente_index_4 = df["IdCliente"][4]
id_cliente_index_4 = df.iloc[4]['IdCliente']
print(f"o ID do cliente no indeci 4 é: { id_cliente_index_4}")
# %%
