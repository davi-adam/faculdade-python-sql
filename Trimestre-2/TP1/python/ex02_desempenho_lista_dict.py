# Exercício 2 - Comparar Tempo de Busca entre Lista e Dicionário
#
# Engenheiros de dados testam o desempenho de diferentes estruturas
# em consultas repetidas. Execute 10.000 buscas pela chave "S3" em
# uma lista de tuplas e em um dicionário, medindo o tempo médio de
# cada operação e exibindo um relatório comparativo.

import time

sensores_lista = [("S1", 34), ("S2", 36), ("S3", 37), ("S4", 38)]
sensores_dict  = {"S1": 34, "S2": 36, "S3": 37, "S4": 38}

tempos_lista = []
tempos_dict  = []

for _ in range(10000):
    inicio = time.time()
    for chave, valor in sensores_lista:
        if chave == "S3":
            break
    tempos_lista.append(time.time() - inicio)

for _ in range(10000):
    inicio = time.time()
    _ = sensores_dict["S3"]
    tempos_dict.append(time.time() - inicio)

media_lista = sum(tempos_lista) / len(tempos_lista)
media_dict  = sum(tempos_dict)  / len(tempos_dict)

print("# Relatório de Comparação de Desempenho")
print(f"- Execuções: 10000")
print(f"- Tempo médio (lista): {media_lista:.6f} segundos")
print(f"- Tempo médio (dicionário): {media_dict:.6f} segundos")