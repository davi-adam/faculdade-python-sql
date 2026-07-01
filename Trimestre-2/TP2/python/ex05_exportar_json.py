# Exercício 5 - Exportar Base de Clientes em JSON
#
# O SJ90 exporta sua base de clientes em JSON para integração com
# parceiros externos. Grave o dicionário em clientes_sj90.json,
# reabra o arquivo e imprima seu conteúdo formatado no terminal.

import json

clientes = {
    "Ana Costa": {"cidade": "RJ", "saldo": 1250.75},
    "Bruno Lima": {"cidade": "SP", "saldo": 980.40}
}

with open("clientes_sj90.json", "w", encoding="utf-8") as arquivo:
    json.dump(clientes, arquivo, ensure_ascii=False, indent=4)

with open("clientes_sj90.json", "r", encoding="utf-8") as arquivo:
    dados = json.load(arquivo)

for nome, info in dados.items():
    print(f"{nome} | Cidade: {info['cidade']} | Saldo: R${info['saldo']:.2f}")