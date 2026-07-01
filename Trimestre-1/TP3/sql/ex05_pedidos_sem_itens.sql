-- Exercício 5 - Pedidos que Não Contêm Itens Específicos
--
-- Projeta, sem repetição, o código do cliente, nome do cliente
-- e código do pedido, excluindo os pedidos que contenham os
-- produtos "Disco de corte de madeira" ou "Pá".

SELECT DISTINCT
    cod_cliente,
    nome_cliente,
    cod_pedido
FROM lojamaterial
WHERE cod_pedido NOT IN (
    SELECT cod_pedido
    FROM lojamaterial
    WHERE nome_produto IN ('Disco de corte de madeira', 'Pá')
);