    -- Exercício 2 - Nome e Idade com Renda Superior a R$12.000
--
-- Lista o nome e a idade das pessoas cuja renda mensal
-- seja superior a 12 mil reais.

SELECT nome, idade
FROM massadados_at
WHERE renda_mensal > 12000;