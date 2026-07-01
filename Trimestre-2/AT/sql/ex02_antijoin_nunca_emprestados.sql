-- Exercício 2 - Anti-Join: Livros Nunca Emprestados
--
-- A biblioteca quer identificar livros que nunca foram emprestados,
-- candidatos a desativação do acervo. O LEFT JOIN mantém todos os livros
-- e o filtro WHERE e.id IS NULL seleciona apenas os sem empréstimo.

SELECT
    l.titulo,
    a.nome AS autor
FROM livros l
LEFT JOIN emprestimos e ON l.id = e.livro_id
JOIN autores a          ON l.autor_id = a.id
WHERE e.id IS NULL;