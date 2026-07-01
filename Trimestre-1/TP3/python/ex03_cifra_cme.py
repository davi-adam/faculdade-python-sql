# Exercício 3 - Definir uma Função com Parâmetros Padrão
#
# Uma equipe de sistemas embarcados implementa a Cifra Modular de Engenharia
# (CME) para ofuscar mensagens entre controladores logísticos. Para cada
# caractere: se for espaço, mantém; se índice par, soma 2 ao ASCII;
# se índice ímpar, subtrai 1. A função recebe uma lista de pedidos e um
# status com valor padrão "Pendente".

def criptografar_cme(lista_pedidos, status="Pendente"):
    for codigo in lista_pedidos:
        mensagem = f"Pedido {codigo}: Status - {status}"
        cifrada = ""
        for i, char in enumerate(mensagem):
            if char == " ":
                cifrada += " "
            elif i % 2 == 0:
                cifrada += chr(ord(char) + 2)
            else:
                cifrada += chr(ord(char) - 1)
        print(cifrada)

pedidos = ["A123", "B456", "C789"]

criptografar_cme(pedidos)
criptografar_cme(pedidos, status="Enviado")