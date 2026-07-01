# Exercício 5 - Escrever a Documentação de uma Função com DocString
#
# Uma equipe de automação logística adaptou o problema da Torre de Hanói
# para simular movimentação de paletes entre três áreas. Crie uma função
# recursiva que resolva o problema para n discos e documente-a com DocString
# explicando propósito, parâmetros e comportamento.

def mover_hanoi(n, origem, destino, suporte):
    """
    Resolve o problema da Torre de Hanói para n discos.

    Parâmetros:
        n (int): número de discos a mover (deve ser >= 1).
        origem  (str): nome da torre de origem.
        destino (str): nome da torre de destino.
        suporte (str): nome da torre auxiliar.

    Comportamento:
        Imprime cada movimento no formato:
        "Mover disco de {origem} para {destino}".
        Não retorna nenhum valor.
    """
    if n == 1:
        print(f"Mover disco de {origem} para {destino}")
        return
    mover_hanoi(n - 1, origem, suporte, destino)
    print(f"Mover disco de {origem} para {destino}")
    mover_hanoi(n - 1, suporte, destino, origem)

mover_hanoi(3, "A", "C", "B")
