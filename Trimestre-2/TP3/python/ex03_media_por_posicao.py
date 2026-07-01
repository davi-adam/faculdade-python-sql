# Exercício 3 - Gerar Tabela Consolidada de Médias por Posição
#
# Estatísticos identificam como as posições evoluem no FIFA.
# Carregue players_20.csv, agrupe por player_positions e calcule
# a média de overall, potential e age. Exiba ordenado pelo overall médio.

import pandas as pd

df = pd.read_csv("players_20.csv")

df_medias = (
    df.groupby("player_positions")[["overall", "potential", "age"]]
    .mean()
    .round(2)
    .sort_values("overall", ascending=False)
    .reset_index()
)

print(df_medias)