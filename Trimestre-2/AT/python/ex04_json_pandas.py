# Exercício 4 - Manipular JSON com Pandas
#
# Os dados salvos em JSON precisam ser analisados pela equipe.
# Carregue dados_scraping.json com pd.read_json, renomeie as colunas
# para português em snake_case e filtre registros lançados nos anos 2000.

import pandas as pd

df = pd.read_json("dados_scraping.json")

df = df.rename(columns={
    "Game": "jogo",
    "Developer(s)": "desenvolvedor",
    "Publisher(s)": "produtor",
    "Release date": "data_publicacao",
    "Sales": "vendas"
})

df_2000 = df[df["data_publicacao"].astype(str).str.startswith("200")]

print(df_2000.to_string(index=False))