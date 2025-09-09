# %%
import pandas as pd
import sqlalchemy
import sqlite3

engine = sqlalchemy.create_engine("sqlite:///../data/database.db")
# %%
clientes = pd.read_sql_table(table_name="clientes", con=engine)
clientes
# %%
clientes.shape
# %%
# nao e  legal pegar todos os dados do banco pq voce vai sobrecarregar a memoria
# a rede o banco entao melhor opcao e usar query
query = "SELECT * FROM clientes LIMIT 100"
df_100 = pd.read_sql_query(query, con=engine)
df_100
# %%
