# Exercício 1 - Download da Página HTML com urllib
#
# Analistas coletam estatísticas públicas sobre jogos mais vendidos
# do PlayStation. Faça o download da página via urllib, salve como
# pagina_original.html e trate falhas de conexão com try/except.

import urllib.request

url = "https://en.wikipedia.org/wiki/List_of_best-selling_PlayStation_video_games"

try:
    with urllib.request.urlopen(url) as resposta:
        conteudo = resposta.read()

    with open("pagina_original.html", "wb") as arquivo:
        arquivo.write(conteudo)

    print("Página salva com sucesso em pagina_original.html")

except urllib.error.URLError as e:
    print(f"Erro de conexão: {e.reason}")
except Exception as e:
    print(f"Erro inesperado: {e}")