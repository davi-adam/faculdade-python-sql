-- Exercício 6 - Perfis Acadêmicos e Técnicos Específicos
--
-- Lista nome e formação dos profissionais que sejam professores
-- ou engenheiros civis com renda a partir de R$11.000, ou que
-- tenham mais de 50 anos nessas mesmas áreas.

SELECT nome, formacao
FROM massadados_at
WHERE profissao IN ('Professor', 'Engenheiro Civil')
  AND (
      renda_mensal >= 11000
      OR idade > 50
  );