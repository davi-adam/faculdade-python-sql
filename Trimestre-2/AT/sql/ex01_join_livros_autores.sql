-- Exercício 1 - INNER JOIN entre Livros e Autores
--
-- A coordenação pediu listagem do acervo identificando o autor de cada livro.
-- O INNER JOIN retorna apenas livros que possuem autor correspondente,
-- ordenados por nome do autor e depois por ano de publicação.

SELECT
    l.titulo,
    a.nome          AS autor,
    l.ano_publicacao
FROM livros l
INNER JOIN autores a ON l.autor_id = a.id
ORDER BY a.nome ASC, l.ano_publicacao ASC;