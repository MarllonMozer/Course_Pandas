# %%
import pandas as pd


# %%
df[QtdePontos > 10]
# %%

brinquedo = pd.DataFrame(
    {
        "nome" : ["marllon", "ana", "bia", "carlos", "daniela"],
        "idade": [5, 32, 17, 53, 64,],
        "uf": ["SP", "RJ", "MG", "MG", "TO"]
    }
)
filtro = brinquedo["idade"] >= 18
brinquedo[filtro]
# %%
df = pd.read_csv("../data/transacoes.csv", sep=";")
df.head()
# %%
filtro = df["QtdePontos"] >= 50 
df[filtro]
# %%
filtro = (df["QtdePontos"] >= 50) & (df["QtdePontos"] < 100)
df[filtro]
# %%
filtro = (df["QtdePontos"] == 1) | (df["QtdePontos"] == 100)
df[filtro]
# %%
