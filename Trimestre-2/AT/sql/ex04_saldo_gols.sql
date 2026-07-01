-- Exercício 4 - Saldo de Gols por Time
--
-- Cada time aparece em partidas como mandante e como visitante.
-- Calculamos gols pró e contra em cada papel separadamente e somamos
-- com GROUP BY. O resultado é ordenado por saldo decrescente.

SELECT
    t.nome,
    SUM(gols_pro)    AS gols_pro,
    SUM(gols_contra) AS gols_contra,
    SUM(gols_pro) - SUM(gols_contra) AS saldo
FROM times t
JOIN (
    SELECT time_mandante_id  AS time_id,
           gols_mandante     AS gols_pro,
           gols_visitante    AS gols_contra
    FROM partidas

    UNION ALL

    SELECT time_visitante_id AS time_id,
           gols_visitante    AS gols_pro,
           gols_mandante     AS gols_contra
    FROM partidas
) calc ON t.id = calc.time_id
GROUP BY t.nome
ORDER BY saldo DESC;