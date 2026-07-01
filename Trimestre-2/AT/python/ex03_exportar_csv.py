# Exercício 3 - Exportar para CSV usando Módulo csv
#
# Analistas compartilham o conjunto de dados processado com equipes
# que usam outras ferramentas. Converta o dicionário estruturado para
# CSV, salve como dados_scraping.csv e trate exceções de escrita.

import csv

# Reutiliza a lista de dicionários gerada pela extração
# (assumindo que 'linhas' foi gerada no exercício anterior)
from ex02_extrair_tabela import linhas

try:
    if linhas:
        with open("dados_scraping.csv", "w", newline="", encoding="utf-8") as arquivo:
            writer = csv.DictWriter(arquivo, fieldnames=linhas[0].keys())
            writer.writeheader()
            writer.writerows(linhas)

        print("Arquivo dados_scraping.csv salvo com sucesso.")
    else:
        print("Nenhum dado para salvar.")

except IOError as e:
    print(f"Erro ao salvar o arquivo: {e}")