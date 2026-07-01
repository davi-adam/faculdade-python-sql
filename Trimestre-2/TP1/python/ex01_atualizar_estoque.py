# Exercício 1 - Atualizar Dicionário de Estoque de Livros
#
# Bibliotecários controlam o acervo com dicionários pré-gerados.
# Crie a função atualizar_estoque(estoque, livro, quantidade) que:
# adicione o livro se não existir, atualize se já existir,
# e remova se a quantidade final for 0. Retorne o dicionário atualizado.

estoque = {
    "Python Crash Course": 4,
    "Clean Code": 2,
    "Automate the Boring Stuff": 0
}

def atualizar_estoque(estoque, livro, quantidade):
    if livro in estoque:
        estoque[livro] += quantidade
    else:
        estoque[livro] = quantidade

    if estoque[livro] <= 0:
        del estoque[livro]

    return estoque

atualizar_estoque(estoque, "Clean Code", 3)
atualizar_estoque(estoque, "Fluent Python", 5)
atualizar_estoque(estoque, "Automate the Boring Stuff", 0)

print(estoque)