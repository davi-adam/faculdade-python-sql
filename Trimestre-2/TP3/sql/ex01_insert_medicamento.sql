-- Exercício 1 - Cadastro de Novo Medicamento
--
-- A farmácia credenciou o laboratório LabVida e precisa incluir no catálogo
-- um novo analgésico. O identificador é gerenciado automaticamente pelo banco.

INSERT INTO medicamentos (nome, categoria, preco, fabricante)
VALUES ('Dipirona Sódica 500mg', 'analgesicos', 12.90, 'LabVida');