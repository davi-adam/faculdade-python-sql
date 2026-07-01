# Exercício 2 - Comparar Tempo de Busca entre Lista e Dicionário
#
# Engenheiros de dados do SJ90 precisam decidir entre listas ou dicionários
# para estruturas de cache. Meça o tempo médio de 10.000 buscas pela chave
# "S3" em cada estrutura, usando uma função para calcular a média dos tempos.

import time

sensores_lista = [("S1", 34), ("S2", 36), ("S3", 37), ("S4", 38)]
sensores_dict  = {"S1": 34, "S2": 36, "S3": 37, "S4": 38}

def calcular_media_tempos(tempos):
    return sum(tempos) / len(tempos)

tempos_lista = []
tempos_dict = []

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

print("# Relatório de Comparação de Desempenho")
print(f"- Execuções: 10000")
print(f"- Tempo médio (lista): {calcular_media_tempos(tempos_lista):.6f} segundos")
print(f"- Tempo médio (dicionário): {calcular_media_tempos(tempos_dict):.6f} segundos")