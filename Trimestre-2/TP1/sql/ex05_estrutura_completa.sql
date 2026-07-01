-- Exercício 5 - Estrutura Completa com Todas as Restrições
--
-- O banco precisa estar pronto para produção com integridade total.
-- Todas as cinco tabelas são criadas com PK, FK, NOT NULL e UNIQUE
-- conforme a especificação, respeitando a ordem de dependências.

CREATE TABLE IF NOT EXISTS alunos (
    id_aluno INTEGER PRIMARY KEY,
    nome     TEXT    NOT NULL,
    email    TEXT    UNIQUE NOT NULL,
    curso    TEXT
);

CREATE TABLE IF NOT EXISTS professores (
    id_professor  INTEGER PRIMARY KEY,
    nome          TEXT    NOT NULL,
    email         TEXT    UNIQUE NOT NULL,
    departamento  TEXT
);

CREATE TABLE IF NOT EXISTS disciplinas (
    id_disciplina     INTEGER PRIMARY KEY,
    nome              TEXT    UNIQUE NOT NULL,
    carga_horaria     INTEGER,
    area_conhecimento TEXT
);

CREATE TABLE IF NOT EXISTS turmas (
    id_turma      INTEGER PRIMARY KEY,
    id_disciplina INTEGER NOT NULL,
    id_professor  INTEGER NOT NULL,
    semestre      TEXT,
    horario       TEXT,
    FOREIGN KEY (id_disciplina) REFERENCES disciplinas(id_disciplina),
    FOREIGN KEY (id_professor)  REFERENCES professores(id_professor)
);

CREATE TABLE IF NOT EXISTS matriculas (
    id_aluno   INTEGER,
    id_turma   INTEGER,
    nota       REAL,
    frequencia INTEGER,
    PRIMARY KEY (id_aluno, id_turma),
    FOREIGN KEY (id_aluno) REFERENCES alunos(id_aluno),
    FOREIGN KEY (id_turma) REFERENCES turmas(id_turma)
);