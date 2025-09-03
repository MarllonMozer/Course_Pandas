# %%
import pandas as pd

df = pd.read_csv("../../data/produtos.csv", sep=";")
qtd_colunas_obj = df.select_dtypes(include="object").shape[1]
print(f"tem {qtd_colunas_obj} colunas do tipo object no arquivo produtos.csv")
# %%
