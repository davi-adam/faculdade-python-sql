-- Exercício 2 - Reajuste de Preços de Medicamentos Genéricos
--
-- A diretoria definiu reajuste de 5% apenas para medicamentos da categoria
-- genericos. O novo preço é calculado diretamente a partir do valor atual,
-- sem afetar nenhuma outra categoria ou campo da tabela.

UPDATE medicamentos
SET preco = preco * 1.05
WHERE categoria = 'genericos';