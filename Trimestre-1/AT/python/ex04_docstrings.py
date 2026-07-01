# Exercício 4 - Implementar e Documentar Funções com DocStrings
#
# Engenheiros de automação de armazéns precisam padronizar utilitários internos
# com documentação clara no padrão Google. Parte A: implemente calcular_distancia()
# a partir da DocString fornecida. Parte B: escreva a DocString completa para
# calcular_velocidade(), já implementada.

def calcular_distancia(passos, tamanho_passo):
    """
    Calcula a distância total percorrida em um armazém.

    Args:
        passos (list of int): Lista de valores inteiros representando
            o número de passos em cada deslocamento.
        tamanho_passo (float): O comprimento de cada passo em metros.
    
    Returns:
        float: A distância total percorrida em metros.
    
    Example:
        >>> calcular_distancia([10, 20, 15], 0.8)
        36.0
    """
    return sum(passos) * tamanho_passo

def calcular_velocidade(distancia, tempo, unidade="m/s"):
    """
    Calcula a velocidade com base em distância e tempo, com suporte a
    diferentes unidades de saída.

    Args:
        distancia (float): Distância percorrida em metros.
        tempo (float): Tempo gasto em segundos. Deve ser maior que zero.
        unidade (str): Unidade de saída da velocidade. Aceita "m/s"
            (padrão), "km/h" ou "mph".

    Returns:
        float: Velocidade calculada na unidade solicitada.
        None: Retornado quando tempo for menor ou igual a zero.

    Example:
        >>> calcular_velocidade(100, 10)
        10.0
        >>> calcular_velocidade(100, 10, unidade="km/h")
        36.0
    """
    if tempo <= 0:
        return None

    velocidade = distancia / tempo

    if unidade == "km/h":
        velocidade *= 3.6
    elif unidade == "mph":
        velocidade *= 2.23694

    return velocidade


print(calcular_distancia([10, 20, 15], 0.8))
print(calcular_velocidade(100, 10))
print(calcular_velocidade(100, 10, unidade="km/h"))

help(calcular_distancia)
help(calcular_velocidade)