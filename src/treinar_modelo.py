import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score

# carregar dados

df = pd.read_csv("dados/dados_sensores.csv")

# variáveis de entrada

X = df[
    [
        "temperatura",
        "umidade",
        "chuva_mm",
        "nivel_rio",
        "velocidade_vento",
        "inclinacao_terreno"
    ]
]

# variável alvo

y = df["risco_real"]

# dividir treino e teste

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# criar modelo

modelo = DecisionTreeClassifier()

modelo.fit(X_train, y_train)

# previsões

previsoes = modelo.predict(X_test)

# métricas

print("\nACURÁCIA:")

print(
    accuracy_score(
        y_test,
        previsoes
    )
)

print("\nRELATÓRIO:\n")

print(
    classification_report(
        y_test,
        previsoes
    )
)

# teste manual

novo_dado = [[
    38,
    25,
    95,
    7,
    20,
    30
]]

resultado = modelo.predict(novo_dado)

print("\nPREVISÃO DO SISTEMA:")

print(resultado[0])