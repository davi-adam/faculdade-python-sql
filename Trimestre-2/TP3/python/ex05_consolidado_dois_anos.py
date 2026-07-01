# Exercício 5 - Consolidar Atributos de Jogadores Âncora entre Dois Anos
#
# A comunidade publica comparativos de evolução anual de jogadores famosos.
# Filtre os 20 jogadores âncora em players_20.csv e players_21.csv e crie
# um DataFrame com short_name, overall_20, overall_21, potential_20 e potential_21.

import pandas as pd

jogadores_ancora = [
    "L. Messi", "Cristiano Ronaldo", "Neymar Jr", "K. De Bruyne",
    "R. Lewandowski", "Kylian Mbappé", "Virgil van Dijk", "M. Salah",
    "K. Benzema", "Sergio Ramos", "T. Kroos", "K. Mbappé",
    "Alisson", "M. ter Stegen", "N. Kanté", "H. Kane",
    "S. Mané", "P. Dybala", "Raheem Sterling", "Son Heung-min"
]

df_20 = pd.read_csv("players_20.csv")
df_21 = pd.read_csv("players_21.csv")

ancora_20 = df_20[df_20["short_name"].isin(jogadores_ancora)][["short_name", "overall", "potential"]]
ancora_21 = df_21[df_21["short_name"].isin(jogadores_ancora)][["short_name", "overall", "potential"]]

df_consolidado = ancora_20.merge(ancora_21, on="short_name", suffixes=("_20", "_21"))

print(df_consolidado.to_string(index=False))