# Exercício 1 - Importação de Arquivos CSV com Pandas
#
# Modders do FIFA carregam tabelas de atributos de CSVs oficiais.
# Importe players_20.csv com Pandas, exiba as cinco primeiras linhas,
# as colunas disponíveis e o número total de registros.

import pandas as pd

df = pd.read_csv("players_20.csv")

print(df.head())
print("\nColunas:", df.columns.tolist())
print(f"Total de registros: {len(df)}")