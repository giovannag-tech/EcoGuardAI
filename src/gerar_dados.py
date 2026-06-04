import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

regioes = [
    "Zona Norte - Área de Enchente",
    "Zona Sul - Área de Deslizamento",
    "Interior SP - Área de Queimada",
    "Litoral SP - Área de Enchente"
]

dados = []

for i in range(200):
    regiao = random.choice(regioes)
    data_hora = datetime.now() - timedelta(hours=i)

    temperatura = round(random.uniform(18, 42), 2)
    umidade = round(random.uniform(20, 95), 2)
    chuva_mm = round(random.uniform(0, 120), 2)
    nivel_rio = round(random.uniform(0.5, 8.0), 2)
    velocidade_vento = round(random.uniform(2, 60), 2)
    inclinacao_terreno = round(random.uniform(0, 45), 2)

    if chuva_mm > 80 or nivel_rio > 6:
        risco = "ALTO"
    elif chuva_mm > 40 or nivel_rio > 4:
        risco = "MEDIO"
    elif temperatura > 35 and umidade < 35:
        risco = "ALTO"
    else:
        risco = "BAIXO"

    dados.append([
        regiao,
        data_hora,
        temperatura,
        umidade,
        chuva_mm,
        nivel_rio,
        velocidade_vento,
        inclinacao_terreno,
        risco
    ])

df = pd.DataFrame(dados, columns=[
    "regiao",
    "data_hora",
    "temperatura",
    "umidade",
    "chuva_mm",
    "nivel_rio",
    "velocidade_vento",
    "inclinacao_terreno",
    "risco_real"
])

df.to_csv("dados/dados_sensores.csv", index=False, encoding="utf-8")

print("Arquivo dados_sensores.csv gerado com sucesso!")