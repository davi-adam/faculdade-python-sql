-- Exercício 5 - Publicação Automática de Episódios Pendentes
--
-- Episódios que ficaram como rascunho mesmo após a data de lançamento
-- devem ser promovidos para publicado. A data atual é determinada
-- dinamicamente. Episódios futuros ou com outros status não são alterados.

UPDATE episodios
SET    status = 'publicado'
WHERE  status = 'rascunho'
  AND  data_lancamento <= DATE('now');