# Exercício 2 - Operações Aritméticas em Contexto Logístico
#
# Uma empresa de logística quer calcular a quilometragem total e o custo
# médio de combustível de entregas urbanas. Cada veículo percorre em média
# 21 km por dia e os gastos diários com combustível são de R$305,00.
# Defina km_por_dia = 21 e gasto_diario = 305 e imprima os resultados de:
# total de km em uma semana, diferença entre R$100 e o gasto diário,
# quantos dias R$500 cobre, o resto do gasto em relação a 100,
# e a média de custo por km.

km_por_dia = 21
gasto_diario = 305

print("Total de km em uma semana:", km_por_dia * 7)
print("Diferença entre R$100 e o gasto diário:", 100 - gasto_diario)
print("Dias cobertos por R$500:", 500 // gasto_diario)
print("Resto do gasto diário em relação a 100:", gasto_diario % 100)
print("Custo médio por km:", gasto_diario / km_por_dia)