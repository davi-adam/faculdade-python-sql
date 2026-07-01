-- Exercício 3 - Agrupamento por Ano de Aposentadoria com Média de Renda
--
-- Agrupa os registros por ano de aposentadoria e apresenta
-- a média da renda mensal para cada grupo.

SELECT
    ano_aposentadoria,
    AVG(renda_mensal) AS media_renda
FROM massadados_at
GROUP BY ano_aposentadoria;