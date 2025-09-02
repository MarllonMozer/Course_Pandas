# %%
import pandas as pd

clientes = pd.read_csv("../data/clientes.csv", sep=";")
clientes.head()
# %%
clientes = clientes.dropna()
# %%
clientes
# %%
uf = pd.read_csv("../data/uf_brasil.csv", sep=";")
uf
# %%
uf = uf.dropna(how="all")
uf
# %%
uf = uf.dropna(how="all", subset=["Bandeira", "Abreviação"])
uf
# %%
df = pd.DataFrame(
    {
        "nome": ["Téo", None, "Nah", "Marcio"],
        "idade": [None, None, 43, 52],
        "salario": [3453,4324,None,5423]
    }
)

# df
df.dropna(how="all", subset=["idade", "nome"])

# %%

df["idade"].fillna(0)
# %%
df.fillna(0)
# %%
df.fillna({
    "nome":"alguem",
    "idade": 0
})
# %%
medias = df[["idade","salario"]].mean()
df.fillna(medias)
# %%
