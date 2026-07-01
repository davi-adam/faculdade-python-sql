-- Exercício 4 - Descontinuação da Tabela de Promoções
--
-- Diferença em relação ao Exercício 3:
-- No Ex. 3 usamos DELETE para esvaziar a tabela — ela continuou existindo
-- para ser reutilizada na próxima campanha.
--
-- Aqui a situação é diferente: a diretoria encerrou definitivamente o programa
-- de promoções. A tabela não tem mais nenhuma função no sistema.
-- O comando adequado agora é DROP TABLE, que remove a tabela completamente
-- do banco — estrutura, dados e tudo mais.
-- Manter uma tabela vazia e sem propósito seria apenas poluição no schema.

DROP TABLE IF EXISTS promocoes_temporarias;