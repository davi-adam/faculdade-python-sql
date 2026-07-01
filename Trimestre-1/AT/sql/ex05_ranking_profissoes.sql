-- Exercício 5 - Ranking de Profissões por Maior Renda Mensal
--
-- Agrupa por profissão e apresenta o valor máximo de renda mensal
-- de cada uma. Lista apenas as profissões com máximo >= R$14.000,
-- ordenadas de forma decrescente.

SELECT
    profissao,
    MAX(renda_mensal) AS maior_renda
FROM massadados_at
GROUP BY profissao
HAVING MAX(renda_mensal) >= 14000
ORDER BY maior_renda DESC;