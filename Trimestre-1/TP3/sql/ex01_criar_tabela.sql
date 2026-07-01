-- Exercício 1 - Criar Banco de Dados e Tabela lojamaterial
--
-- Criação do banco de dados loja_material.db e da tabela principal
-- com todos os campos necessários para registrar produtos, pedidos
-- e clientes da loja de materiais.
-- Nota: o banco foi criado via Python com sqlite3 e os dados
-- inseridos a partir do arquivo Insert_loja_material.txt.

CREATE TABLE IF NOT EXISTS lojamaterial (
    cod_produto       TEXT,
    nome_produto      TEXT,
    categoria_produto TEXT,
    valor_produto     REAL,
    cod_pedido        TEXT,
    cod_cliente       TEXT,
    nome_cliente      TEXT,
    tipo_cliente      TEXT,
    qtd_comprada      INTEGER,
    subtotal          REAL
);