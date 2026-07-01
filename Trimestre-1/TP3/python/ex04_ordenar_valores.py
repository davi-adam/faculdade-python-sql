# Exercício 4 - Definir uma Função que Retorne Valores
#
# Uma equipe de ciência de dados para logística precisa ordenar amostras de
# desempenho de sensores sem usar bibliotecas externas. Crie uma função que
# receba uma lista de números, ordene do menor para o maior usando for e
# trocas condicionais, e retorne a lista ordenada.

def ordenar_valores(valores):
    valores = list(valores)
    for i in range(len(valores)):
        for j in range(i + 1, len(valores)):
            if valores[j] < valores[i]:
                valores[i], valores[j] = valores[j], valores[i]
    return valores

print(ordenar_valores([42, 7, 19, 3, 88, 25]))