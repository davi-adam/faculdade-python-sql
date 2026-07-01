# Exercício 3 - Funções com Valores de Retorno
#
# Uma equipe de ciência de dados educacional precisa estruturar um pipeline
# modular de cálculo de desempenho. Implemente três funções encadeadas:
# calcular_media(), arredondar_media() e classificar_desempenho(), passando
# o retorno de uma como entrada da próxima.

def calcular_media(notas, pesos):
    total_pesos = sum(pesos)
    media = sum(n * p for n, p in zip(notas, pesos)) / total_pesos
    return media

def arrendondar_media(media):
    return round(media, 1)

def classificar_desempenho(media):
    if media < 2.5:
        return "ND"
    elif media < 5.0:
        return "D"
    elif media < 7.5:
        return "DL"
    else:
        return "DML"

def executar_pipeline(notas, pesos):
    media_final = arrendondar_media(calcular_media(notas, pesos))
    classificacao_final = classificar_desempenho(media_final)

    print(f"Notas: {notas}")
    print(f"Pesos: {pesos}\n")
    print(f"Média calculada:   {calcular_media(notas, pesos):.2f}")
    print(f"Média arredondada: {media_final}")
    print(f"Classificação final: {classificacao_final}\n")

executar_pipeline([8.0, 6.5, 9.0], [2, 3, 5])
executar_pipeline([4.0, 3.5, 2.0], [1, 2, 3])