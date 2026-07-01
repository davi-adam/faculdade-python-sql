# Exercício 6 - Otimizar Verificação de Sensores
#
# Uma equipe de controle de qualidade precisa verificar a temperatura de
# vários sensores. O código original repete o mesmo bloco para cada sensor.
# Reescreva usando uma lista e um laço de repetição para verificar quais
# sensores estão acima do limite de 30°C.

temperaturas = [28, 31, 27, 35, 29]

for i, temp in enumerate(temperaturas):
    if temp > 30:
        print(f"Sensor {i + 1} acima do limite")