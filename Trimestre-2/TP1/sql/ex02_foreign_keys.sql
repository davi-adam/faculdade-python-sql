-- Exercício 2 - Aplicar FOREIGN KEYs para Integridade Referencial
--
-- Cada matrícula deve referenciar obrigatoriamente um aluno e uma turma
-- válidos. As FOREIGN KEYs garantem que não existam matrículas órfãs
-- no banco de dados.

CREATE TABLE IF NOT EXISTS matriculas (
    id_aluno INTEGER,
    id_turma INTEGER,
    nota REAL,
    frequencia INTEGER,
    PRIMARY KEY (id_aluno, id_turma),
    FOREIGN KEY (id_aluno) REFERENCES alunos(id_aluno),
    FOREIGN KEY (id_turma) REFERENCES turmas(id_turma)
);