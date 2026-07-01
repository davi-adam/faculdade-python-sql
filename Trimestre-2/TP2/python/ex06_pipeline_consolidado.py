# Exercício 6 - Consolidar Saldos e Gerar Relatório Final
#
# O Banco SJ90 unifica dados de clientes_premium.json e transacoes.csv
# em um relatório analítico. Para cada cliente, calcule total de créditos,
# total de débitos e saldo final. Salve como relatorio_sj90.csv e exiba
# ordenado por saldo_final decrescente.

import json
import pandas as pd

# Leitura dos arquivos
with open("clientes_premium.json", "r", encoding="utf-8") as arquivo:
    clientes_premium = json.load(arquivo)

df_transacoes = pd.read_csv("transacoes.csv")

# Agrupamento de créditos e débitos por cliente
creditos = df_transacoes[df_transacoes["tipo"] == "credito"].groupby("cliente")["valor"].sum()
debitos = df_transacoes[df_transacoes["tipo"] == "debito"].groupby("cliente")["valor"].sum()

# Montagem do relatório
registros = []
for nome, info in clientes_premium.items():
    saldo_inicial = info["saldo"]
    total_creditos = creditos.get(nome, 0)
    total_debitos = debitos.get(nome, 0)
    saldo_final = saldo_inicial + total_creditos + total_debitos

    registros.append({
        "cliente": nome,
        "saldo_inicial": saldo_inicial,
        "total_creditos": total_creditos,
        "total_debitos": total_debitos,
        "saldo_final": saldo_final
    })

df_relatorio = pd.DataFrame(registros).sort_values("saldo_final", ascending=False)
df_relatorio.to_csv("relatorio_sj90.csv", index=False)

print(df_relatorio.to_string(index=False))