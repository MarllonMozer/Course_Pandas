# %%
# 06.01 - Qual a quantidade média de redes sociais dos usuários?
# E a Variância? E o máximo?

import pandas as pd

clientes = pd.read_csv("../../data/clientes.csv", sep=";")
clientes.head()

# %%

clientes["totalRedes"] = (clientes['FlEmail'] + 
                          clientes['FlTwitch'] + 
                          clientes['FlYouTube'] + 
                          clientes['FlBlueSky'] +
                          clientes['FlInstagram'])

media = clientes["totalRedes"].mean()
variancia = clientes["totalRedes"].var()
maximo = clientes["totalRedes"].max()

print("media:",media)
print("variancia:",variancia)
print("maximo:",maximo)

# %%

redes = [
    "FlEmail",
    "FlTwitch",
    "FlYouTube",
    "FlBlueSky",
    "FlInstagram",
]

clientes[redes].sum(axis=1).describe()