-- Exercício 5 - Corrigir Query Quebrada de Artilheiros
--
-- Defeitos encontrados na query original:
--
-- 1. LEFT JOIN em vez de INNER JOIN com gols:
--    O LEFT JOIN inclui jogadores sem gols, mas o HAVING COUNT(*) > 1
--    os excluiria de qualquer forma. Porém COUNT(*) conta a linha nula
--    do LEFT JOIN como 1, distorcendo o resultado. O correto é
--    INNER JOIN para contar apenas gols reais.
--
-- 2. WHERE COUNT(*) > 1:
--    Funções de agregação não podem ser usadas no WHERE.
--    O filtro por agregação deve estar no HAVING.
--
-- 3. GROUP BY j.nome sem incluir t.nome:
--    Todas as colunas não agregadas no SELECT devem aparecer no GROUP BY.
--
-- 4. ORDER BY gols ASC (padrão):
--    O enunciado pede do maior para o menor. Faltava DESC.

SELECT
    j.nome,
    t.nome      AS time,
    COUNT(*)    AS gols
FROM jogadores j
INNER JOIN gols  g ON g.jogador_id = j.id
JOIN       times t ON j.time_id    = t.id
GROUP BY j.nome, t.nome
HAVING COUNT(*) > 1
ORDER BY gols DESC;