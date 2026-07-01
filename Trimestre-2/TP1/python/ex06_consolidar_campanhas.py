# Exercício 6 - Consolidar Bases e Exportar para JSON
#
# Analistas de marketing reúnem cadastros de clientes de três campanhas.
# Elimine duplicatas usando sets, una as bases em uma lista única
# e exporte o resultado consolidado para um arquivo JSON.

import json

campanha_1 = ["Ana", "Bruno", "Carla"]
campanha_2 = ["Bruno", "Daniel", "Eduardo"]
campanha_3 = ["Ana", "Fernanda", "Gustavo"]

clientes_unicos = list(set(campanha_1) | set(campanha_2) | set(campanha_3))
clientes_unicos.sort()

with open("clientes_consolidados.json", "w", encoding="utf-8") as arquivo:
    json.dump(clientes_unicos, arquivo, ensure_ascii=False, indent=4)

print(f"Total de clientes únicos: {len(clientes_unicos)}")
print(clientes_unicos)