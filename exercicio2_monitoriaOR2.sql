CREATE OR REPLACE TYPE tp_mercadoria AS OBJECT (
    codigo NUMBER,
    nome VARCHAR2(50),
    preco DECIMAL(7,2)
);
/

CREATE OR REPLACE TYPE tp_item AS OBJECT (
    numero NUMBER,
    quantidade NUMBER,
    mercadoria REF tp_mercadoria
);
/

CREATE OR REPLACE TYPE tp_nt_item AS TABLE OF tp_item;
/

CREATE OR REPLACE TYPE tp_pedido AS OBJECT (
    numero NUMBER,
    data_pedido DATE,
    data_entrega DATE,
    item tp_nt_item
);
/

CREATE TABLE tb_mercadoria OF tp_mercadoria(
    codigo PRIMARY KEY
);
/

CREATE TABLE tb_pedido OF tp_pedido 
    NESTED TABLE tp_nt_item
    STORE AS (nt_items)(
    numero PRIMARY KEY
);
/

INSERT INTO tb_mercadoria
VALUES(tp_mercadoria(
    001,
    'Madeira',
    500,00
));
/
INSERT INTO tb_mercadoria
VALUES(tp_mercadoria(
    002,
    'Cimento',
    50,00
));
/
INSERT INTO tb_mercadoria
VALUES(tp_mercadoria(
    003,
    'Tábua',
    250,00
));
/
-- Pedidos
INSERT INTO tb_pedido
VALUES(tp_pedido(
    0001,
    to_date('05/03/2022', 'dd/mm/yyyy'),
    to_date('07/03/2022', 'dd/mm/yyyy'),
    
));