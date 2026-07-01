# Exercício 6 - Identificação de Substrings Palíndromas em Janelas de Texto
#
# Pesquisadores em NLP precisam detectar palíndromos em janelas de comprimento
# fixo dentro de uma string. Implemente janelas_palindromas(s, k) de duas
# formas: tradicional com for/if e como one-liner com list comprehension.

def janelas_palindromas(s, k):
    resultado = []
    for i in range(len(s) - k + 1):
        janela = s[i:i + k]
        if janela == janela[::-1]:
            resultado.append(janela)
    return resultado

def janelas_palindromas_oneliner(s, k):
    return [s[i:i + k] for i in range(len(s) - k + 1) if s[i:i + k] == s[i:i + k][::-1]]

print(janelas_palindromas("banana", 3))
print(janelas_palindromas_oneliner("banana", 3))