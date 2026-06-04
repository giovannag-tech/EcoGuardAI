CREATE TABLE regioes (
    id_regiao SERIAL PRIMARY KEY,
    nome_regiao VARCHAR(100),
    cidade VARCHAR(100),
    estado VARCHAR(50),
    tipo_area VARCHAR(50)
);

CREATE TABLE sensores (
    id_sensor SERIAL PRIMARY KEY,
    id_regiao INT REFERENCES regioes(id_regiao),
    tipo_sensor VARCHAR(50),
    status VARCHAR(30)
);

CREATE TABLE leituras_sensores (
    id_leitura SERIAL PRIMARY KEY,
    id_regiao INT REFERENCES regioes(id_regiao),
    data_hora TIMESTAMP,
    temperatura FLOAT,
    umidade FLOAT,
    chuva_mm FLOAT,
    nivel_rio FLOAT,
    velocidade_vento FLOAT,
    inclinacao_terreno FLOAT,
    risco_real VARCHAR(30)
);

CREATE TABLE alertas (
    id_alerta SERIAL PRIMARY KEY,
    id_regiao INT REFERENCES regioes(id_regiao),
    data_hora TIMESTAMP,
    tipo_alerta VARCHAR(50),
    nivel_risco VARCHAR(30),
    mensagem TEXT
);