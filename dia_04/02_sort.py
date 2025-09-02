# %%
import pandas as pd

clientes = pd.read_csv("../data/clientes.csv", sep=";")
clientes.head()
# %%
clientes["QtdePontos"].sort_values()
# %%
max_ponto = clientes["QtdePontos"].max()
filtro =  clientes["QtdePontos"] == max_ponto
clientes[filtro]
# %%
clientes.sort_values(by="QtdePontos")
# %%
clientes.sort_values(by="QtdePontos", ascending=False).head()
# %%

users = pd.DataFrame(
    {
        "nome": ["teo", "marllon", "vanda", "wagner"],
        "idade": [54, 53, 22, 22],
        "salario": [1500, 1508, 3600, 1508],
    }
)
users
# %%
users.sort_values(by=["salario","idade"], ascending=[False, True])
# %%
