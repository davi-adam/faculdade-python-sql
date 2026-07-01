-- Exercício 4 - Profissionais com Renda Acima da Média Geral
--
-- Lista o nome e a renda mensal dos profissionais cuja renda
-- seja superior à média de todos os registros da tabela,
-- utilizando subquery.

SELECT nome, renda_mensal
FROM massadados_at
WHERE renda_mensal > (
    SELECT AVG(renda_mensal)
    FROM massadados_at
);