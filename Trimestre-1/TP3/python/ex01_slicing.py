# Exercício 1 - Realizar Slicing com Diferentes Intervalos
#
# Em um sistema de rastreamento de equipamentos médicos, os técnicos utilizam
# códigos padronizados como "MON2023-RN456-P01" para identificar tipo, série
# e ponto de uso. Extraia o ano, o segmento intermediário e os dois últimos
# caracteres usando apenas slicing.

codigo_sensor = "MON2023-RN456-P01"

ano = codigo_sensor[3:7]
categoria = codigo_sensor[8:13]
unidade = codigo_sensor[-2:]

print("Ano:", ano)
print("Categoria:", categoria)
print("Unidade:", unidade)