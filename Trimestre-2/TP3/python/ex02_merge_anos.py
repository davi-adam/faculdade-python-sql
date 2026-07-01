# Exercício 2 - Combinar Dados de Anos Diferentes
#
# Analistas estudam a evolução de overall e potencial entre anos.
# Carregue players_20.csv e players_21.csv, filtre os jogadores âncora
# em ambos, realize merge por short_name e long_name e crie um DataFrame
# consolidado com overall e potential de cada ano.

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

ancora_20 = df_20[df_20["short_name"].isin(jogadores_ancora)][["short_name", "long_name", "overall", "potential"]]
ancora_21 = df_21[df_21["short_name"].isin(jogadores_ancora)][["short_name", "long_name", "overall", "potential"]]

df_merge = ancora_20.merge(ancora_21, on=["short_name", "long_name"], suffixes=("_20", "_21"))

print(df_merge)