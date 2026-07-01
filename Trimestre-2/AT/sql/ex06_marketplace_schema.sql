-- Exercício 6 - Schema Completo do Marketplace Artesanal Normalizado
--
-- A planilha original viola as três formas normais:
-- 1FN: coluna 'categorias' armazena múltiplos valores separados por ";".
-- 2FN: dados de cliente e vendedor repetem em cada linha de item de pedido.
-- 3FN: vend_pix depende de vend_email (atributo não-chave), não do pedido.
--
-- O modelo abaixo normaliza essas estruturas em entidades separadas,
-- com PKs, FKs, UNIQUE e NOT NULL conforme as regras de negócio.

CREATE TABLE IF NOT EXISTS clientes (
    cliente_id INTEGER PRIMARY KEY,
    nome       TEXT    NOT NULL,
    email      TEXT    UNIQUE NOT NULL,
    cidade     TEXT
);

CREATE TABLE IF NOT EXISTS vendedores (
    vendedor_id INTEGER PRIMARY KEY,
    nome        TEXT    NOT NULL,
    email       TEXT    UNIQUE NOT NULL
);

-- Relação 1:1 entre vendedor e conta bancária (regra 5)
CREATE TABLE IF NOT EXISTS contas_bancarias (
    conta_id    INTEGER PRIMARY KEY,
    vendedor_id INTEGER UNIQUE NOT NULL,
    chave_pix   TEXT    NOT NULL,
    FOREIGN KEY (vendedor_id) REFERENCES vendedores(vendedor_id)
);

CREATE TABLE IF NOT EXISTS categorias (
    categoria_id INTEGER PRIMARY KEY,
    nome         TEXT    UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS produtos (
    produto_id  INTEGER PRIMARY KEY,
    nome        TEXT    NOT NULL,
    preco_atual REAL    NOT NULL,
    vendedor_id INTEGER NOT NULL,
    FOREIGN KEY (vendedor_id) REFERENCES vendedores(vendedor_id)
);

-- Relacionamento N:N entre produtos e categorias (regra 4)
CREATE TABLE IF NOT EXISTS produto_categorias (
    produto_id   INTEGER,
    categoria_id INTEGER,
    PRIMARY KEY (produto_id, categoria_id),
    FOREIGN KEY (produto_id)   REFERENCES produtos(produto_id),
    FOREIGN KEY (categoria_id) REFERENCES categorias(categoria_id)
);

CREATE TABLE IF NOT EXISTS pedidos (
    pedido_id  TEXT    PRIMARY KEY,
    data       TEXT    NOT NULL,
    cliente_id INTEGER NOT NULL,
    FOREIGN KEY (cliente_id) REFERENCES clientes(cliente_id)
);

-- O preço no momento da compra é registrado aqui (regra 7)
CREATE TABLE IF NOT EXISTS itens_pedido (
    item_id    INTEGER PRIMARY KEY,
    pedido_id  TEXT    NOT NULL,
    produto_id INTEGER NOT NULL,
    quantidade INTEGER NOT NULL,
    preco_unit REAL    NOT NULL,
    FOREIGN KEY (pedido_id)  REFERENCES pedidos(pedido_id),
    FOREIGN KEY (produto_id) REFERENCES produtos(produto_id)
);

-- Inserção dos dados normalizados da planilha
INSERT INTO clientes VALUES
    (1, 'Marina Costa',  'marina@mail.com', 'São Paulo'),
    (2, 'Tiago Reis',    'tiago@mail.com',  'Curitiba'),
    (3, 'Larissa Veiga', 'lari@mail.com',   'Recife');

INSERT INTO vendedores VALUES
    (1, 'Atelier Lua',   'lua@atelier.com.br'),
    (2, 'Tecidos Nelm',  'nelm@tecidos.com.br'),
    (3, 'Madeira Viva',  'madv@artesa.com.br');

INSERT INTO contas_bancarias VALUES
    (1, 1, 'lua-pix-01'),
    (2, 2, 'nelm-pix-02'),
    (3, 3, 'madv-pix-03');

INSERT INTO categorias VALUES
    (1, 'decoração'), (2, 'cerâmica'), (3, 'casa'),
    (4, 'têxtil'),    (5, 'madeira'),  (6, 'cozinha');

INSERT INTO produtos VALUES
    (1, 'Vaso de cerâmica azul',       85.00,  1),
    (2, 'Almofada bordada flores',     45.00,  2),
    (3, 'Porta-copos rústico (kit 4)', 60.00,  3),
    (4, 'Tábua de queijo entalhada',   110.00, 3);

INSERT INTO produto_categorias VALUES
    (1,1),(1,2),(2,3),(2,4),(2,1),(3,3),(3,5),(4,6),(4,5);

INSERT INTO pedidos VALUES
    ('P001', '2026-04-10', 1),
    ('P002', '2026-04-11', 2),
    ('P003', '2026-04-12', 1),
    ('P004', '2026-04-15', 3);

INSERT INTO itens_pedido VALUES
    (1, 'P001', 1, 2, 85.00),
    (2, 'P001', 2, 1, 45.00),
    (3, 'P002', 1, 1, 85.00),
    (4, 'P003', 3, 1, 60.00),
    (5, 'P003', 2, 2, 45.00),
    (6, 'P004', 4, 1, 110.00);

-- Query de verificação: reconstrói uma linha da planilha original
SELECT
    p.pedido_id,
    p.data,
    c.nome          AS cliente,
    v.nome          AS vendedor,
    pr.nome         AS produto,
    ip.preco_unit,
    ip.quantidade
FROM itens_pedido ip
JOIN pedidos  p  ON ip.pedido_id  = p.pedido_id
JOIN clientes c  ON p.cliente_id  = c.cliente_id
JOIN produtos pr ON ip.produto_id = pr.produto_id
JOIN vendedores v ON pr.vendedor_id = v.vendedor_id
ORDER BY p.pedido_id, pr.nome;