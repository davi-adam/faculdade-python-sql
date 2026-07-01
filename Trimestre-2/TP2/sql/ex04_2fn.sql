-- Exercício 4 - Aplicar a Segunda Forma Normal (2FN)
--
-- Na 2FN, nenhum atributo não-chave pode depender de apenas parte da
-- chave composta. O campo price depende apenas do livro, não da venda,
-- e por isso permanece em Books. O total_value é calculado a partir de
-- price e quantity, eliminando dependências parciais.

CREATE TABLE IF NOT EXISTS Sales (
    sale_id    INTEGER PRIMARY KEY,
    book_id    INTEGER NOT NULL,
    quantity   INTEGER NOT NULL,
    sale_date  TEXT    NOT NULL,
    FOREIGN KEY (book_id) REFERENCES Books(book_id)
);

-- total_value calculado a partir de Books.price * Sales.quantity
-- evita redundância e garante consistência
SELECT
    s.sale_id,
    b.title,
    b.price,
    s.quantity,
    b.price * s.quantity AS total_value
FROM Sales s
JOIN Books b ON s.book_id = b.book_id;