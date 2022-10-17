DROP TABLE tb_aluno;
DROP TYPE tp_varr_responsavel;
DROP TYPE tp_responsavel;
DROP TYPE tp_varr_telefone;
DROP TYPE tp_telefone;
DROP TYPE tp_aluno;

CREATE OR REPLACE TYPE tp_telefone AS OBJECT (
    cod_area NUMBER,
    telefone NUMBER
);
/

CREATE OR REPLACE TYPE tp_varr_telefone AS VARRAY(3) OF tp_telefone;
/

CREATE OR REPLACE TYPE tp_responsavel AS OBJECT (
    nome VARCHAR2(50),
    telefone tp_varr_telefone
);
/

CREATE OR REPLACE TYPE tp_varr_responsavel AS VARRAY(2) OF tp_responsavel;
/

CREATE OR REPLACE TYPE tp_aluno AS OBJECT (
    nome VARCHAR2(50),
    matricula NUMBER,
    responsaveis tp_varr_responsavel,
    
    CONSTRUCTOR FUNCTION tp_aluno (SELF IN OUT NOCOPY tp_aluno,
        nome VARCHAR2,
        matricula NUMBER,
        responsaveis tp_varr_responsavel)
        RETURN SELF AS RESULT
);
/

CREATE OR REPLACE TYPE BODY tp_aluno AS
    CONSTRUCTOR FUNCTION tp_aluno (SELF IN OUT tp_aluno,
        nome VARCHAR2,
        matricula NUMBER,
        responsaveis tp_varr_responsavel) RETURN SELF AS RESULT IS
        BEGIN
            SELF.nome := nome;
            SELF.matricula := matricula;
            SELF.responsaveis := responsaveis;
            RETURN;
        END;
END;
/

CREATE TABLE tb_aluno OF tp_aluno (
    matricula PRIMARY KEY
);
/

