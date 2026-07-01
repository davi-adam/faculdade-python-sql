-- Exercício 3 - Relacionamento N:N entre Livros e Autores
--
-- Um livro pode ter vários autores e um autor pode escrever vários livros.
-- A tabela BookAuthors resolve esse relacionamento N:N com uma chave
-- composta e FKs para Books e Authors.

CREATE TABLE IF NOT EXISTS Authors (
    author_id   INTEGER PRIMARY KEY,
    author_name TEXT    NOT NULL
);

CREATE TABLE IF NOT EXISTS BookAuthors (
    book_id   INTEGER,
    author_id INTEGER,
    PRIMARY KEY (book_id, author_id),
    FOREIGN KEY (book_id)   REFERENCES Books(book_id),
    FOREIGN KEY (author_id) REFERENCES Authors(author_id)
);

INSERT INTO Authors VALUES (1, 'Machado de Assis');
INSERT INTO Authors VALUES (2, 'Clarice Lispector');

INSERT INTO BookAuthors VALUES (1, 1);
INSERT INTO BookAuthors VALUES (2, 2);

-- Listar autores por livro
SELECT b.title, a.author_name
FROM BookAuthors ba
JOIN Books   b ON ba.book_id   = b.book_id
JOIN Authors a ON ba.author_id = a.author_id;