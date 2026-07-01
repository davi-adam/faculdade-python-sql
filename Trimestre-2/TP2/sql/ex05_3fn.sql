-- Exercício 5 - Aplicar a Terceira Forma Normal (3FN)
--
-- Na 3FN, nenhum atributo não-chave pode depender de outro atributo
-- não-chave. A cidade da editora depende da editora, não do livro.
-- Mantê-la em Publishers elimina a dependência transitiva
-- Books → publisher_id → publisher_city.

ALTER TABLE Publishers ADD COLUMN publisher_city TEXT;

UPDATE Publishers SET publisher_city = 'São Paulo' WHERE publisher_id = 1;
UPDATE Publishers SET publisher_city = 'Rio de Janeiro' WHERE publisher_id = 2;

-- Consulta que demonstra a estrutura sem dependência transitiva
SELECT
    b.title,
    p.publisher_name,
    p.publisher_city
FROM Books b
JOIN Publishers p ON b.publisher_id = p.publisher_id;