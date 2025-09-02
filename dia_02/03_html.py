# %% 
import pandas as pd
df = pd.read_clipboard()
df
# %%
url = "https://pt.wikipedia.org/wiki/Unidades_federativas_do_Brasil"
dfs = pd.read_html(url)
dfs
# %%
len(dfs)  # Quantas tabelas foram lidas
# %%
df_uf = dfs[1]
df_uf.to_csv("../data/uf_brasil.csv", index=False, sep=";")
# %%
df_uf2 = pd.read_csv("../data/uf_brasil.csv", sep=";")
df_uf2
# %%
