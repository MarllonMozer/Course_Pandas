# %%
import pandas as pd

df_clientes = pd.read_csv("../../data/clientes.csv", sep=";")
num_linhas_clientes = df_clientes.shape[0]
num_linhas_clientes

print(f"tem {num_linhas_clientes} de linhas no arquivo clientes.csv")
