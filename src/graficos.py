import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dados/dados_sensores.csv")

plt.figure(figsize=(8,5))

plt.scatter(
    df["umidade"],
    df["temperatura"]
)

plt.xlabel("Umidade (%)")
plt.ylabel("Temperatura (°C)")
plt.title("Análise dos Sensores Ambientais")

plt.savefig("imagens/grafico_sensores.png")

plt.show()

print("Gráfico criado com sucesso!")