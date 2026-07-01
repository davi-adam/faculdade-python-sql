# Exercício 5 - Converter Dicionário em JSON
#
# Desenvolvedores de e-commerce exportam dados de produtos para sistemas
# de integração que leem JSON. Exporte o dicionário produtos para um arquivo
# produtos.json, reabra o arquivo, carregue os dados e verifique o tipo
# do objeto retornado.

import json

produtos = {
    "Smartphone": {"preco": 2500, "estoque": 12},
    "Notebook": {"preco": 4800, "estoque": 5},
    "Fone Bluetooth": {"preco": 300,  "estoque": 25}
}

with open("produtos.json", "w", encoding="utf-8") as arquivo:
    json.dump(produtos, arquivo, ensure_ascii=False, indent=4)

with open("produtos.json", "r", encoding="utf-8") as arquivo:
    dados = json.load(arquivo)

print(type(dados))
print(dados)