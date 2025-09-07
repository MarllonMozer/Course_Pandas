# %% 
import re
from arrow import get
import pandas as pd

df = pd.read_csv("../data/clientes.csv", sep=";")
df.head()
# %%
idCliente = "000ff655-fa9f-4baa-a108-47f581ec52a1"
df["IdCliente"].str[24:]
# %%
def get_last_id(x):
    return x.split("-")[-1]

idCliente.split("-")[-1]
# %%
get_last_id("001749bd-37b5-4b1e-8111-f9fbba90f530")
# %%
id_novo = []
for i in df["IdCliente"]:
    novo = get_last_id(i)
    id_novo.append(novo)
    #id_novo.append(get_last_id(i))

df["novo_id"] = id_novo
df.head()
# %%
df["IdCliente"].apply(get_last_id)

# %%
