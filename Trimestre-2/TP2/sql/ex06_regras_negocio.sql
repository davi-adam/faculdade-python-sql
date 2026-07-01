-- Exercício 6 - Estabelecer Regras de Negócio
--
-- A equipe financeira define regras que garantem coerência entre cadastros
-- e operação comercial. As consultas de validação identificam violações
-- sem depender de restrições automáticas do banco.

-- Regra 1: o preço de um livro não pode ser zero ou negativo
SELECT * FROM Books WHERE price <= 0;

-- Regra 2: a quantidade vendida não pode ser negativa
SELECT * FROM Sales WHERE quantity < 0;

-- Como as regras de negócio complementam as formas normais:
-- As formas normais garantem estrutura sem redundância e dependências corretas.
-- As regras de negócio garantem que os valores inseridos fazem sentido
-- para o domínio da aplicação. Juntas, asseguram integridade estrutural
-- e semântica do banco de dados.

-- Futuramente essas validações poderiam ser automatizadas com:
-- CHECK (price > 0) na criação da tabela, ou
-- triggers que disparam antes de INSERT/UPDATE para barrar valores inválidos.