# %%
import pandas as pd

url = "https://pt.wikipedia.org/wiki/Unidades_federativas_do_Brasil"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}
dfs = pd.read_html(url, storage_options=headers)

uf = dfs[1]
# %%
uf.dtypes
# %%
numero = "1 247 689,5"
numero = float(numero.replace(" ", "").replace(",", "."))
type(numero)
# %%

def str_to_float(x:str):
    x =  float(x.replace(" ", "")
               .replace(",", ".")
               .replace("\xa0", ""))
    return x

uf["[Área (km²)"] = uf["Área (km²)"].apply(str_to_float)
uf["População (Censo 2022)"] = uf["População (Censo 2022)"].apply(str_to_float)
uf["PIB (2015)"] = uf["PIB (2015)"].apply(str_to_float)
uf["PIB per capita (R$) (2015)"] = uf["PIB per capita (R$) (2015)"].apply(str_to_float)
uf
# %%
area_nova = []
for i in uf["Área (km²)"]:
    area_nova.append(str_to_float(i))

uf["nova_area"] = area_nova
uf.head()
# %%
x = "71,6 anos"

def exp_to_anos(exp):
    return float(exp.replace(",",".")
                 .replace(" anos", ""))

uf["Expectativa de vida (2016)"] = uf["Expectativa de vida (2016)"].apply(exp_to_anos)
uf
# %%

def uf_to_regiao(uf):
   
    if uf in ["Distrito Federal", "Goiás", "Mato Grosso", "Mato Grosso do Sul"]:
        return "Centro-Oeste"
    elif uf in ["Alagoas","Bahia", "Ceará", "Maranhão", "Paraíba", "Pernambuco", "Piauí", "Rio Grande do Norte", "Sergipe"]:
        return "Nordeste"
    elif uf in ["Acre", "Amapá", "Amazonas", "Pará", "Rondônia", "Roraima", "Tocantins"]:
       return "Norte"
    elif uf in ["Espírito Santo","Minas Gerais", "Rio de Janeiro", "São Paulo"]:
        return "Sudeste"
    elif uf in ["Paraná", "Rio Grande do Sul", "Santa Catarina"]:
        return "Sul"
    
uf["Região"] = uf["Unidade federativa"].apply(uf_to_regiao)
uf
# %%
def mortalidade_to_float(x):
   x = float(x.replace("‰", "")
               .replace(",", "."))
   return x
uf["Mortalidade infantil (/1000)"] = uf["Mortalidade infantil (2016)"].apply(mortalidade_to_float)

# %%

linha  = uf.iloc[6]
(linha["PIB per capita (R$) (2015)"] > 30000 and 
linha["Mortalidade infantil (/1000)"] < 15  and 
linha["IDH (2010)"] > 700)
# %%

def classifica_bom(linha):
    return(linha["PIB per capita (R$) (2015)"] > 30000 and 
           linha["Mortalidade infantil (/1000)"] < 15  and 
           linha["IDH (2010)"] > 700)

# %%
#apliquei nas linhas 
uf.apply(classifica_bom, axis= 1)
# %%
