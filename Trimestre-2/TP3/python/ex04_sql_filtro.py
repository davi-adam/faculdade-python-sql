# Exercício 4 - Exportar DataFrame para SQL e Recuperar com Consulta
#
# Modders exportam bases temporárias para SQL para uso posterior.
# Carregue players_21.csv, grave no banco em memória como jogadores_21
# e recupere via SQL apenas os jogadores com overall acima de 88.

import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv("players_21.csv")

engine = create_engine("sqlite:///:memory:")
df.to_sql("jogadores_21", engine, if_exists="replace", index=False)

resultado = pd.read_sql_query("SELECT * FROM jogadores_21 WHERE overall > 88", engine)

print(resultado[["short_name", "overall", "potential"]].to_string(index=False))