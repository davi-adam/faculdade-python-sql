# Exercício 3 - Remover Leituras Incorretas
#
# Pesquisadores de meteorologia eliminam medições inválidas de um
# dicionário de temperaturas por estação. Crie filtrar_temperaturas()
# que remova valores abaixo de -50 e retorne o dicionário limpo,
# imprimindo o número de entradas removidas e o total restante.

temperaturas = {
    "RJ": 29.4, "SP": -99.0, "MG": 27.2, "BA": 31.1, "RS": -88.0
}

def filtrar_temperaturas(temp_dict):
    removidas = [chave for chave, valor in temp_dict.items() if valor < -50]
    for chave in removidas:
        del temp_dict[chave]

    print(f"Entradas removidas: {len(removidas)}")
    print(f"Total restante: {len(temp_dict)}")
    return temp_dict

print(filtrar_temperaturas(temperaturas))