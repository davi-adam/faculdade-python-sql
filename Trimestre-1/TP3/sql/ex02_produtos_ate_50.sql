-- Exercício 2 - Quantos Produtos Distintos com Valor até R$50
--
-- Conta quantos produtos distintos existem na tabela com valor
-- menor ou igual a R$50,00.

SELECT COUNT(DISTINCT nome_produto) AS total_produtos
FROM lojamaterial
WHERE valor_produto <= 50;