# %%

from cycler import K
import pandas as pd

df = pd.DataFrame({ 
      "nome": ['marllon','ana','joao','ana','lucas','joao','teo','joao'],
      "sobrenome":["dias",'luiza','silva','agnelo','dias','silva','agnelo','silva']
    })

df
# %%
# ele vai manter a primeira
df.drop_duplicates()
# %%
# posso escolher qual manter com o keep mas nao da pra manter as do meio 
# pode ter varias no meio
df.drop_duplicates(keep='last')
# %%
df = pd.DataFrame({ 
      "nome": ['marllon','ana','joao','ana','lucas','joao','teo','joao'],
      "sobrenome":["dias",'luiza','silva','agnelo','dias','silva','agnelo','silva'],
      "salario":[6500,2345,8954,2345,3453,2400,5432,4788]
    })
df
# %%
df_sort = df.sort_values("salario", ascending=False)
df_sort

# %%
df_sort.drop_duplicates(subset=["nome", "sobrenome"])
# %%
df_sort = (df.sort_values("salario", ascending=False)
            .drop_duplicates(keep = 'last',subset=["nome", "sobrenome"]))
# %%
