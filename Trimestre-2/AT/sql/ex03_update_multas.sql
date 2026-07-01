-- Exercício 3 - UPDATE de Multas em Aberto com Reajuste de 50%
--
-- A direção reajustou em 50% as multas de empréstimos ainda em aberto
-- que já possuem multa registrada. Apenas linhas com data_devolucao_real
-- nula e valor_multa maior que zero são afetadas.

UPDATE emprestimos
SET    valor_multa = valor_multa * 1.5
WHERE  data_devolucao_real IS NULL
  AND  valor_multa > 0;

SELECT id, livro_id, membro_id, valor_multa
FROM emprestimos
WHERE data_devolucao_real IS NULL
  AND valor_multa > 0;