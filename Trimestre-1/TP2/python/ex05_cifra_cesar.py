# Exercício 5 - Decodificar Mensagem Cifrada
#
# Você recebeu uma mensagem encriptada: "SbwKrQ eh phokRu q MDydvfulsW"
# A chave é o número de vezes que as letras D, d e W aparecem na mensagem.
# Use a cifra de César para decodificá-la. Apenas palavras com mais de 3
# caracteres estão encriptadas. Não use split().

mensagem_cifrada = "SbwKrQ eh phokRu q MDydvfulsW"

chave = mensagem_cifrada.count("D") + mensagem_cifrada.count("d") + mensagem_cifrada.count("W")

mensagem_decifrada = ""
i = 0

while i < len(mensagem_cifrada):
    char = mensagem_cifrada[i]

    if char == " ":
        mensagem_decifrada += " "
        i += 1
        continue

    inicio_palavra = 1
    palavra = ""
    while i < len(mensagem_cifrada) and mensagem_cifrada[i] != " ":
        palavra += mensagem_cifrada[i]
        i += 1
    
    if len(palavra) > 3:
        decifrada = ""
        for c in palavra:
            if c.upper() == c and c.isalpha():
                decifrada += chr((ord(c) - ord("A") - chave) % 26 + ord("A"))
            elif c.lower() == c and c.isalpha():
                decifrada += chr((ord(c) - ord("a") - chave) % 26 + ord("a"))
            else:
                decifrada += c
        mensagem_decifrada += decifrada
    else:
        mensagem_decifrada += palavra

print(mensagem_decifrada)