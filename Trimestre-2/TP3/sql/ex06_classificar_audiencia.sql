-- Exercício 6 - Classificação Automática de Podcasts por Audiência
--
-- A coluna faixa_audiencia está vazia para todos os registros e precisa
-- ser preenchida em uma única instrução com CASE, aplicando a regra:
-- menos de 1.000 reproduções → nicho
-- entre 1.000 e 49.999 → medio
-- 50.000 ou mais → popular

UPDATE podcasts
SET faixa_audiencia = CASE
    WHEN total_reproducoes < 1000  THEN 'nicho'
    WHEN total_reproducoes < 50000 THEN 'medio'
    ELSE 'popular'
END;