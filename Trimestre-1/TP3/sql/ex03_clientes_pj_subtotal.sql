-- Exercício 3 - Clientes Pessoa Jurídica com Subtotal >= R$100
--
-- Projeta, sem repetição, o código, nome e tipo dos clientes
-- cujo subtotal seja maior ou igual a R$100 e o tipo seja
-- Pessoa Jurídica. Os campos são renomeados com alias.

SELECT DISTINCT
    cod_cliente  AS "Código",
    nome_cliente AS "Nome",
    tipo_cliente AS "Tipo"
FROM lojamaterial
WHERE subtotal     >= 100
  AND tipo_cliente  = 'Pessoa Jurídica';