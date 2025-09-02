# %%

import pandas as pd

clientes = pd.read_csv("../data/clientes.csv", sep=";")
clientes.head()
# %%
filtro = clientes["QtdePontos"] == 0
clientes_0 = clientes[filtro]
clientes_0["flag_1"] = 1
# %%
clientes_0
# %%
A = [1,2]
B = A
print("A:", A)
print("B:", B)

B.append("QUALQUER COISA")
print("A:", A)
print("B:", B)
# porque em python a variavel nao copia a outra ela extende da outra
# a forma para resolver isso e colocar o copy
# %%
#os filtros seguem a mesma regra
#isso pode custar mais memoria e voce vai estar duplicando dados,
#mas dessa forma voce desassocia as variaveis
A = [1,2]
B = A.copy()
print("A:", A)
print("B:", B)

B.append("QUALQUER COISA")
print("A:", A)
print("B:", B)

# %%
filtro = clientes["QtdePontos"] == 0
clientes_0 = clientes[filtro].copy()
clientes_0["flag_1"] = 1

# %%
clientes_0
# %%
