import pandas as pd
import psycopg2

# conexão com PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    database="ecoguard_ai",
    user="postgres",
    password="postgres123"
)

cursor = conn.cursor()

# ler csv
df = pd.read_csv("dados/dados_sensores.csv")

# inserir regiões únicas
regioes_inseridas = {}

for regiao in df["regiao"].unique():

    cursor.execute("""
        INSERT INTO regioes
        (nome_regiao, cidade, estado, tipo_area)
        VALUES (%s,%s,%s,%s)
        RETURNING id_regiao
    """,
    (
        regiao,
        "São Paulo",
        "SP",
        "Monitoramento Ambiental"
    ))

    id_regiao = cursor.fetchone()[0]

    regioes_inseridas[regiao] = id_regiao

# inserir leituras

for _, row in df.iterrows():

    cursor.execute("""
        INSERT INTO leituras_sensores
        (
            id_regiao,
            data_hora,
            temperatura,
            umidade,
            chuva_mm,
            nivel_rio,
            velocidade_vento,
            inclinacao_terreno,
            risco_real
        )
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """,
    (
        regioes_inseridas[row["regiao"]],
        row["data_hora"],
        row["temperatura"],
        row["umidade"],
        row["chuva_mm"],
        row["nivel_rio"],
        row["velocidade_vento"],
        row["inclinacao_terreno"],
        row["risco_real"]
    ))

conn.commit()

cursor.close()
conn.close()

print("Dados inseridos com sucesso!")