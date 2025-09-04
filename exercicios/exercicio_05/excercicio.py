# %%
import pandas as pd
import numpy as np
from sqlalchemy import true

clientes = pd.read_csv("../../data/clientes.csv", sep=";")
clientes
# %%
# 05.01 - Crie uma coluna nova “twitch_points” que e resultado da multiplicação do 
# saldo de pontos e a marcação da twitch
clientes["twitch_points"] = clientes["QtdePontos"] * clientes["FlTwitch"]
clientes.head()
# %%
# 05.02 - Aplique o log na coluna de saldo de pontos, criando uma coluna nova
clientes["logPontos"] = np.log(clientes["QtdePontos"])
clientes.head()
# %%
# 05.03 - Crie uma coluna que sinalize se a pessoa tem vínculo com alguma
#(qualquer uma) plataforma de rede social.
clientes["TemRedeSocial"] = clientes["FlEmail"] + clientes["FlTwitch"] + clientes["FlYouTube"] + clientes["FlBlueSky"] + clientes["FlInstagram"] >= 1
clientes.head()
# %%
#05.04 - Qual é o id de cliente que tem maior saldo de pontos? E o menor?
clientes.sort_values(by="QtdePontos", ascending=True).head(1)["IdCliente"]
clientes.sort_values(by="QtdePontos", ascending=False).head(1)["IdCliente"]
# %%
# 05.05 - Selecione a primeira transação diária de cada cliente.