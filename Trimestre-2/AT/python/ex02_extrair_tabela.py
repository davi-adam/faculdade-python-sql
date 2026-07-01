# Exercício 2 - Extração de Tabela com BeautifulSoup
#
# A equipe extrai a tabela principal da página salva localmente.
# Abra pagina_original.html com BeautifulSoup, localize a primeira
# tabela estruturada, extraia cabeçalhos e linhas em uma lista de
# dicionários e exiba os cinco primeiros registros.

from bs4 import BeautifulSoup

try:
    with open("pagina_original.html", "r", encoding="utf-8") as arquivo:
        soup = BeautifulSoup(arquivo, "html.parser")

    tabela = soup.find("table")
    headers = [th.get_text(strip=True) for th in tabela.find_all("th")]
    linhas = []

    for tr in tabela.find_all("tr")[1:]:
        celulas = [td.get_text(strip=True) for td in tr.find_all("td")]
        if celulas:
            linhas.append(dict(zip(headers, celulas)))

    for linha in linhas[:5]:
        print(linha)

except FileNotFoundError:
    print("Arquivo pagina_original.html não encontrado.")
except AttributeError:
    print("Tabela não encontrada na página.")