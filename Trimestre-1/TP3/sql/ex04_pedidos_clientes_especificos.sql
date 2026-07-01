-- Exercício 4 - Códigos de Pedidos de Clientes Específicos
--
-- Projeta, sem repetição, os códigos dos pedidos dos clientes
-- "Banco Bem Ricos" e "João", utilizando o operador IN.

SELECT DISTINCT cod_pedido
FROM lojamaterial
WHERE nome_cliente IN ('Banco Bem Ricos', 'João');