# Exercício 5 - Criar e Consultar Banco SQL com SQLAlchemy
#
# A comunidade armazena dados em banco relacional leve para consultas
# rápidas. Crie uma engine SQLite em memória, carregue dados_scraping.csv
# na tabela tabela_scraping e execute uma consulta SQL com pd.read_sql_query.

import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite:///:memory:")

df = pd.read_csv("dados_scraping.csv")
df.to_sql("tabela_scraping", engine, if_exists="replace", index=False)

resultado = pd.read_sql_query("SELECT * FROM tabela_scraping LIMIT 10", engine)

print(resultado.to_string(index=False))