# Exercício 6 - Relatório Longitudinal de Atributos FIFA 15 a 21
#
# A comunidade publica relatório completo da evolução de jogadores
# entre FIFA 15 e FIFA 21. Carregue os 7 CSVs, filtre os jogadores
# âncora, consolide overall e potential por ano, calcule evolução
# e classifique tendência. Salve como relatorio_fifa_15_21_sj90.csv.

import pandas as pd

jogadores_ancora = [
    "L. Messi", "Cristiano Ronaldo", "Neymar Jr", "K. De Bruyne",
    "R. Lewandowski", "Kylian Mbappé", "Virgil van Dijk", "M. Salah",
    "K. Benzema", "Sergio Ramos", "T. Kroos", "K. Mbappé",
    "Alisson", "M. ter Stegen", "N. Kanté", "H. Kane",
    "S. Mané", "P. Dybala", "Raheem Sterling", "Son Heung-min"
]

anos = [15, 16, 17, 18, 19, 20, 21]
df_base = None

for ano in anos:
    df = pd.read_csv(f"players_{ano:02d}.csv")
    df_ano = df[df["short_name"].isin(jogadores_ancora)][["short_name", "overall", "potential"]].copy()
    df_ano = df_ano.rename(columns={"overall": f"overall_{ano}", "potential": f"potential_{ano}"})

    if df_base is None:
        df_base = df_ano
    else:
        df_base = df_base.merge(df_ano, on="short_name", how="outer")

df_base["evolucao_overall_15_21"]   = df_base["overall_21"]   - df_base["overall_15"]
df_base["evolucao_potential_15_21"] = df_base["potential_21"] - df_base["potential_15"]

def classificar_tendencia(valor):
    if valor > 1:
        return "subiu"
    elif valor < -1:
        return "caiu"
    return "estavel"

df_base["tendencia_overall"] = df_base["evolucao_overall_15_21"].apply(classificar_tendencia)
df_base.to_csv("relatorio_fifa_15_21_sj90.csv", index=False)

print(df_base[["short_name", "overall_15", "overall_21", "evolucao_overall_15_21", "tendencia_overall"]].to_string(index=False))