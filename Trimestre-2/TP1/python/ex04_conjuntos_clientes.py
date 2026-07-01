# Exercício 4 - Analisar Interseção e Diferença entre Conjuntos
#
# Analistas de CRM identificam clientes exclusivos e comuns entre
# duas bases. Calcule interseção, diferença e união entre os conjuntos
# clientes_A e clientes_B, exibindo cada resultado com título descritivo
# e o número total de clientes únicos.

clientes_A = {"Ana", "Bruno", "Carla", "Daniel"}
clientes_B = {"Bruno", "Carla", "Eduardo", "Fernanda"}

intersecao = clientes_A & clientes_B
exclusivos_A = clientes_A - clientes_B
exclusivos_B = clientes_B - clientes_A
uniao = clientes_A | clientes_B

print("Clientes em comum:", intersecao)
print("Exclusivos da base A:", exclusivos_A)
print("Exclusivos da base B:", exclusivos_B)
print("Total de clientes únicos:", len(uniao))