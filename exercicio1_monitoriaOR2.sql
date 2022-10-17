CREATE OR REPLACE TYPE tp_telefone AS OBJECT (
    telefone VARCHAR(11)
);
/

CREATE OR REPLACE TYPE tp_varr_telefone AS VARRAY(5) OF tp_telefone;
/

CREATE OR REPLACE TYPE tp_cliente AS OBJECT (
    codigo NUMBER,
    nome VARCHAR2(50),
    telefone tp_varr_telefone
);
/

CREATE TABLE tb_cliente OF tp_cliente (
    codigo PRIMARY KEY
);
/


INSERT INTO tb_cliente
VALUES(tp_cliente(
    01,
    'Gustavo Borges',
    tp_varr_telefone(
        tp_telefone('81994711791'),
        tp_telefone('81993329902'),
        tp_telefone('81866668888'),
        tp_telefone('81932224449'),
        tp_telefone('81922300049')
    )
));
/
INSERT INTO tb_cliente
VALUES(tp_cliente(
    02,
    'Carolina Borges',
    tp_varr_telefone(
        tp_telefone('81994811791'),
        tp_telefone('81993789902')
    )
    
));
/
INSERT INTO tb_cliente
VALUES(tp_cliente(
    03,
    'Eduarda Brandão',
    tp_varr_telefone(
        tp_telefone('81994711700')
    )
));
/
INSERT INTO tb_cliente
VALUES(tp_cliente(
    04,
    'Yuri Monteiro',
    tp_varr_telefone(
        tp_telefone('81994509791'),
        tp_telefone('81993324602'),
        tp_telefone('81862268888')
    )
    
));
/
INSERT INTO tb_cliente
VALUES(tp_cliente(
    05,
    'Hugo Araujo',
    tp_varr_telefone(
        tp_telefone('81965711791'),
        tp_telefone('81987329902'),
        tp_telefone('81819668888'),
        tp_telefone('81933224449'),
        tp_telefone('81922309949')
    )
));
/