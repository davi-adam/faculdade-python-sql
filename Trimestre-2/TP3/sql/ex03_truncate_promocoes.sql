-- Exercício 3 - Limpeza ao Fim da Campanha Mensal
--
-- O comando adequado aqui é TRUNCATE (ou DELETE sem WHERE no SQLite),
-- pois precisamos esvaziar a tabela mantendo sua estrutura intacta
-- para receber a próxima campanha.
--
-- Diferente do DROP TABLE, que removeria a tabela completamente do banco,
-- o TRUNCATE apenas remove os dados, preservando colunas, tipos e restrições.
-- Isso é essencial porque a tabela será reutilizada no próximo ciclo.

DELETE FROM promocoes_temporarias;