-- Exercício 2 - Criar Tabela Publishers com Relacionamento 1:N
--
-- Cada livro pertence a uma única editora, mas uma editora pode publicar
-- vários livros. A FOREIGN KEY em Books referencia Publishers,
-- representando corretamente a cardinalidade 1:N.

CREATE TABLE IF NOT EXISTS Publishers (
    publisher_id   INTEGER PRIMARY KEY,
    publisher_name TEXT    NOT NULL
);

ALTER TABLE Books ADD COLUMN publisher_id INTEGER REFERENCES Publishers(publisher_id);

INSERT INTO Publishers VALUES (1, 'Companhia das Letras');
INSERT INTO Publishers VALUES (2, 'Rocco');

UPDATE Books SET publisher_id = 1 WHERE book_id = 1;
UPDATE Books SET publisher_id = 2 WHERE book_id = 2;