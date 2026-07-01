-- Exercício 1 - Criar a Tabela Books com Chaves e Restrições
--
-- A livraria precisa garantir que cada livro seja identificado unicamente
-- para evitar duplicidades no estoque. A tabela Books recebe PRIMARY KEY,
-- ISBN com restrição UNIQUE e campos obrigatórios com NOT NULL.

CREATE TABLE IF NOT EXISTS Books (
    book_id  INTEGER PRIMARY KEY,
    title    TEXT    NOT NULL,
    genre    TEXT,
    price    REAL    NOT NULL,
    isbn     TEXT    UNIQUE
);

-- Teste de restrição: tentativa de inserir ISBN duplicado
INSERT INTO Books VALUES (1, 'Dom Casmurro',   'Romance', 39.90, 'ISBN-001');
INSERT INTO Books VALUES (2, 'A Hora da Estrela', 'Romance', 34.90, 'ISBN-002');

-- Esta linha deve falhar por ISBN duplicado:
-- INSERT INTO Books VALUES (3, 'Outro Livro', 'Ficção', 29.90, 'ISBN-001');