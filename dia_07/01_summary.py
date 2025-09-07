# %%

from http import client
import pandas as pd

idades = [22, 35, 46, 27, 19, 30, 41, 18, 23, 50, 33, 26, 39, 28, 31, 77]
idades = pd.Series(idades)
idades
# %%
idades.sum()
# %%
idades.min()
# %%
idades.max()
# %%
idades.mean()
# %%
idades.describe()
# %%
clientes = pd.read_csv("../data/clientes.csv", sep=";")
clientes 
# %%
clientes["FlTwitch"].sum()
# %%
clientes["FlTwitch"].mean()
# %%
redes_sociais = ["FlEmail", "FlTwitch", "FlYouTube", "FlBlueSky", "FlInstagram"]
clientes[redes_sociais].mean()
# %%
filtro = clientes.dtypes == "object"
clientes.dtypes[filtro]
# %%
# seu eu quiser negar eu coloco o ~
filtro = clientes.dtypes == "object"
clientes.dtypes[~filtro].index.tolist()
# %%
# outra forma de fazer
num_colums = clientes.dtypes[~(clientes.dtypes == "object")].index.tolist()
clientes[num_colums].mean()
# %%
clientes[num_colums].describe()
# %%
clientes[["FlTwitch", "FlEmail"]].describe()
# %%
