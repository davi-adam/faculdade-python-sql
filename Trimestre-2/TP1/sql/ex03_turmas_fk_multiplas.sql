-- Exercício 3 - Múltiplas FOREIGN KEYs na Tabela Turmas
--
-- Cada turma deve estar vinculada a uma disciplina e a um professor.
-- As FOREIGN KEYs garantem que não existam turmas com dados
-- incompletos ou referências inválidas.

CREATE TABLE IF NOT EXISTS turmas (
    id_turma INTEGER PRIMARY KEY,
    id_disciplina INTEGER NOT NULL,
    id_professor INTEGER NOT NULL,
    semestre TEXT,
    horario TEXT,
    FOREIGN KEY (id_disciplina) REFERENCES disciplinas(id_disciplina),
    FOREIGN KEY (id_professor)  REFERENCES professores(id_professor)
);