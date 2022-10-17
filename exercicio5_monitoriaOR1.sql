DROP TABLE tb_possui;
DROP TABLE tb_endereco;
DROP TABLE tb_cliente;
DROP TYPE tp_possui;
DROP TYPE tp_cliente;
DROP TYPE tp_endereco;

CREATE OR REPLACE TYPE tp_endereco AS OBJECT ( 
    cep NUMBER, 
    bairro VARCHAR2(40), 
    cidade VARCHAR2(40), 
     
    CONSTRUCTOR FUNCTION tp_endereco (SELF IN OUT NOCOPY tp_endereco, 
        cep NUMBER, 
        bairro VARCHAR2, 
        cidade VARCHAR2) RETURN SELF AS RESULT 
); 
/

CREATE OR REPLACE TYPE BODY tp_endereco AS 
     
    CONSTRUCTOR FUNCTION tp_endereco (SELF IN OUT tp_endereco, 
        cep NUMBER, 
        bairro VARCHAR2, 
        cidade VARCHAR2) RETURN SELF AS RESULT IS
        BEGIN 
            SELF.cep := cep; 
            SELF.bairro := bairro; 
            SELF.cidade := cidade; 
            RETURN; 
        END; 
END; 
/
CREATE OR REPLACE TYPE tp_cliente AS OBJECT ( 
    nome VARCHAR2(80), 
    cpf NUMBER,
    endereco REF tp_endereco,
     
    CONSTRUCTOR FUNCTION tp_cliente (SELF IN OUT NOCOPY tp_cliente, 
        nome VARCHAR2, 
        cpf NUMBER,
        endereco tp_endereco) RETURN SELF AS RESULT 
); 
/
CREATE OR REPLACE TYPE BODY tp_cliente AS 
     
    CONSTRUCTOR FUNCTION tp_cliente (SELF IN OUT tp_cliente, 
        nome VARCHAR2, 
        cpf NUMBER,
        endereco tp_endereco) RETURN SELF AS RESULT IS
        BEGIN 
            SELF.nome := nome; 
            SELF.cpf := cpf;
            SELF.endereco := endereco;
            RETURN; 
        END; 
END; 
/
CREATE TABLE tb_cliente OF tp_cliente (
    cpf PRIMARY KEY
);
/
CREATE TABLE tb_endereco OF tp_endereco (
    cep PRIMARY KEY
);
/

-- 3 ENDEREÇO
INSERT INTO tb_endereco
VALUES(tp_endereco(
    5555555,
    'Aflitos',
    'Recife'
));
/
INSERT INTO tb_endereco
VALUES(tp_endereco(
    3333333,
    'Torre',
    'Recife'
));
/
INSERT INTO tb_endereco
VALUES(tp_endereco(
    4444444,
    'Campo grande',
    'Recife'
));
/
-- 3 CLIENTES
INSERT INTO tb_cliente
VALUES(tp_cliente(
    'Gustavo Borges',
    66666666666,
    (SELECT REF(E) FROM tb_endereco E WHERE cep = 5555555)
));
/
INSERT INTO tb_cliente
VALUES(tp_cliente(
    'Eduarda Brandão',
    88888888888,
    (SELECT REF(E) FROM tb_endereco E WHERE cep = 3333333)
));
/
INSERT INTO tb_cliente
VALUES(tp_cliente(
    'Elisabete Oliveira',
    99999999999,
    (SELECT REF(E) FROM tb_endereco E WHERE cep = 4444444)
));
/