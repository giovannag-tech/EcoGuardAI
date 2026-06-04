import psycopg2
import random

conn = psycopg2.connect(
    host="localhost",
    database="ecoguard_ai",
    user="postgres",
    password="postgres123"
)

cursor = conn.cursor()

tipos = [
    "Risco de enchente",
    "Risco de deslizamento",
    "Risco de queimadas"
]

for i in range(10):
    cursor.execute("""
        INSERT INTO alertas(tipo_alerta, nivel_risco)
        VALUES (%s,%s)
    """, (
        random.choice(tipos),
        random.choice(["BAIXO", "MEDIO", "ALTO"])
    ))

conn.commit()

cursor.close()
conn.close()

print("Alertas criados!")