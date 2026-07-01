# Exercício 6 - Combinar Função, Parâmetros Nomeados e Retorno Formatado
#
# Em um ambiente industrial, uma equipe constrói um parser que interpreta
# mensagens brutas de sensores. Tokens válidos começam com "@" e terminam
# com "#". Crie uma função que extraia esses tokens, remova caracteres
# inválidos e retorne uma lista limpa. Sem regex ou bibliotecas externas.

def extrair_codigos(mensagem):
    codigos = []
    i = 0
    while i < len(mensagem):
        if mensagem[i] == "@":
            i += 1
            token = ""
            while i < len(mensagem) and mensagem[i] != "#":
                token += mensagem[i]
                i += 1
            codigo_limpo = ""
            for char in token:
                if char.isalnum():
                    codigo_limpo += char
            if codigo_limpo:
                codigos.append(codigo_limpo)
        i += 1
    return codigos

mensagem = "Sensor detectado: @A1B2C3# fora de faixa. Erro: @ 9X # ignorado. Validação: @99Z#"
print(extrair_codigos(mensagem))