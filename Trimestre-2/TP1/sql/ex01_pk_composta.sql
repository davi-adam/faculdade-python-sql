-- Exercício 1 - Modelar Chave Primária Composta
--
-- A equipe de registros da SJ90 identificou tentativas de matrícula
-- duplicada. Para impedir que um aluno se matricule mais de uma vez
-- na mesma turma, define-se uma PRIMARY KEY composta entre id_aluno
-- e id_turma na tabela matriculas.

CREATE TABLE IF NOT EXISTS matriculas (
    id_aluno INTEGER,
    id_turma INTEGER,
    nota REAL,
    frequencia INTEGER,
    PRIMARY KEY (id_aluno, id_turma)
);