# Exercício 4 - Remover Contas Inativas
#
# O setor de operações do SJ90 remove mensalmente contas sem movimentação
# há mais de 12 meses. Crie remover_inativas(contas, limite) que remova
# do dicionário as contas acima do limite, retorne o dicionário atualizado
# e imprima um relatório com as contas removidas e restantes.

contas_inativas = {
    "C101": 5,  "C102": 13, "C103": 8,
    "C104": 15, "C105": 3,  "C106": 24, "C107": 11
}

def remover_inativas(contas, limite):
    removidas = [cod for cod, meses in contas.items() if meses > limite]
    for cod in removidas:
        del contas[cod]

    print(f"Contas removidas: {removidas}")
    print(f"Contas restantes: {contas}")
    return contas

remover_inativas(contas_inativas, 12)