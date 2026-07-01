-- Exercício 1 - Criar Tabela massadados_at
--
-- Criação da tabela com estrutura adequada para armazenar os dados
-- do arquivo de inserts do Assessment. Os tipos foram definidos
-- com base nos dados fornecidos no arquivo massadados_at_inserts.txt.

CREATE TABLE IF NOT EXISTS massadados_at (
    id                  INTEGER PRIMARY KEY,
    nome                TEXT,
    idade               INTEGER,
    profissao           TEXT,
    nacionalidade       TEXT,
    formacao            TEXT,
    renda_mensal        REAL,
    ano_aposentadoria   INTEGER,
    licenca_especial    TEXT
);