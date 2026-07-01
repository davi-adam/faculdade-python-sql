# Exercício 2 - Condicionais com Operadores Booleanos
#
# Gestores de saúde pública precisam classificar pacientes em faixas de risco
# para triagem inicial. A partir de idade, temperatura e frequência cardíaca,
# aplique if/elif/else com operadores booleanos para classificar como:
# Baixo, Moderado, Alto, Crítico ou Emergência.

idade = 15
temperatura = 39.5
freq_card = 110

if idade < 18 and temperatura >= 39.0:
    classificacao = "Crítico"
elif temperatura >= 38.5 or freq_card >= 120:
    classificacao = "Alto"
elif idade >= 60 or (temperatura >= 37.5 and freq_card < 120):
    classificacao = "Moderado"
elif idade >= 18 and temperatura < 37.5 and freq_card < 100:
    classificacao = "Baixo"
else:
    classificacao = "Emergência"

print(f"Paciente classificado como: {classificacao}")