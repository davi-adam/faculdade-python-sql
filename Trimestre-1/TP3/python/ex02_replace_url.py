# Exercício 2 - Substituir Partes de uma String com replace()
#
# Em um curso de desenvolvimento web, alunos precisam manipular URLs de busca.
# Substitua "velho" por "novo" na URL usando replace(). Em seguida, crie uma
# função que extraia o valor do parâmetro "termo" da URL, sem usar bibliotecas
# externas, suportando pequenas variações no formato.

url = "https://sistema.exemplo.com/busca?termo=velho"
url_atualizada = url.replace("velho", "novo")

def extrair_termo(url):
    inicio = url.find("termo=")
    if inicio == -1:
        return None
    inicio += len("termo=")
    fim = url.find("&", inicio)
    if fim == -1:
        return url[inicio:]
    return url[inicio:fim]

print("URL atualizada:", url_atualizada)
print("Termo extraído:", extrair_termo(url_atualizada))