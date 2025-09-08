# %%
import pandas as pd

df_geral = pd.read_csv("../../data/ipea/homicidios.csv", sep=";")
df_geral = df_geral.rename(columns={"valor": "homicidios"})
df_geral = df_geral.set_index(["nome", "período"])
df_geral = df_geral.drop(["cod"], axis=1)
df_geral.head()
# %%
df_negros = pd.read_csv("../../data/ipea/homicidios-negros.csv", sep=";")
df_negros = df_negros.rename(columns={"valor":"homicidios-negros"})
df_negros = df_negros.set_index(["nome", "período"])
df_negros = df_negros.drop(["cod"], axis=1)
df_negros.head()
# %%
pd.concat([df_geral, df_negros], axis= 1)
# %%
#fazendo para todos os arquivos
import pandas as pd
import os

def read_file(file_name:str):
    df = (pd.read_csv(f"../../data/ipea/{file_name}.csv", sep=";")
            .rename(columns={"valor":file_name})
            .set_index(["nome", "período"])
            .drop(["cod"],axis=1))
    
    return df

# %%
file_names = os.listdir("../../data/ipea/")
file_names
# %%
dfs = []
for i in file_names:
    file_name = i.split(".")[0]
    dfs.append(read_file(file_name))


df_full = (pd.concat(dfs, axis=1)
             .reset_index()
             .sort_values(["período", "nome"]))

df_full.to_csv("homicios_consolidado.csv", index=False, sep=";")
# %%
df_full