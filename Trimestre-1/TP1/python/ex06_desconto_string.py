# Exercício 6 - Cálculo de Desconto com Conversão de String
#
# As Óticas SJ90 promovem uma campanha onde o desconto aplicado é
# proporcional à idade do cliente. O sistema recebe a idade como string
# e divide por 3.14 para calcular o percentual de desconto.
# O valor fixo do produto é R$599,99.
# Defina desconto_txt = '21', converta para float, divida por 3.14,
# calcule o desconto sobre R$599,99 e imprima o valor final a pagar.

desconto_txt = "21"
desconto_num = float(desconto_txt) / 3.14

valor_produto = 599.99
valor_desconto = valor_produto * (desconto_num / 100)
valor_final = valor_produto - valor_desconto

print(f"Percentual de desconto: {desconto_num:.2f}")
print(f"Valor final a pagar: R$ {valor_final:.2f}")