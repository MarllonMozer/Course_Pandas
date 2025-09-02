# %%
import pandas as pd
import numpy as np
from sqlalchemy import true

df = pd.read_csv("../data/clientes.csv", sep=";")
df.head()
# %%
df["pontos_100"] = df["QtdePontos"] + 100
df.head()
#%%
df["QtdePontos"] = df["QtdePontos"] + 100
df.head()
# %%
nova_coluna = []
for i in df["QtdePontos"]:
    nova_coluna.append(i+100)

nova_coluna    
# %%
df["emailTwitch"] = df["FlEmail"] + df["FlTwitch"]
df.head()
# %%
df["FlEmail"] * df["FlTwitch"]
# %%
df["qtdeSocial"] = df["FlEmail"] + df["FlTwitch"] + df["FlYouTube"] + df["FlBlueSky"] + df["FlInstagram"]
df
# %%
df["todas_qtdeSocial"] = df["FlEmail"] * df["FlTwitch"] * df["FlYouTube"] * df["FlBlueSky"] * df["FlInstagram"]
df
# %%
df["logPontos"] = np.log(df["QtdePontos"]+1)
df["logPontos"].describe()
# %%
import matplotlib.pyplot as plt

plt.hist(df["logPontos"])
plt.grid(True)
plt.show()

# %%
