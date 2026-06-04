# 🌱 EcoGuard AI

Sistema inteligente de monitoramento ambiental para agricultura, utilizando Inteligência Artificial, Machine Learning, PostgreSQL, Visão Computacional e Dashboard Interativo.

O projeto tem como objetivo auxiliar na identificação de riscos ambientais, como enchentes, deslizamentos e queimadas, por meio da análise de dados simulados de sensores.

---

## 🎯 Objetivo

Desenvolver uma solução inteligente capaz de monitorar condições ambientais, classificar situações de risco e apoiar a tomada de decisão preventiva.

---

## 🚀 Tecnologias Utilizadas

- Python
- PostgreSQL
- Pandas
- Scikit-Learn
- Streamlit
- Plotly
- OpenCV
- Git e GitHub

---

## 🧠 Funcionalidades

- Geração de dados ambientais simulados
- Armazenamento das leituras em banco PostgreSQL
- Classificação automática de riscos com Machine Learning
- Dashboard interativo com filtros e gráficos
- Visão computacional para análise de folhas
- Sistema de alertas ambientais

---

## 🏗️ Arquitetura do Projeto

O EcoGuard AI foi desenvolvido com uma arquitetura simples e integrada:

1. Geração de dados ambientais simulados.
2. Armazenamento das leituras no PostgreSQL.
3. Processamento dos dados com Python.
4. Treinamento do modelo de Machine Learning.
5. Geração de alertas ambientais.
6. Visualização dos resultados no Dashboard.
7. Análise complementar com Visão Computacional.

---

## 📂 Estrutura do Projeto

```text
EcoGuardAI/
├── banco/
│   └── criar_tabelas.sql
├── dados/
│   └── dados_sensores.csv
├── imagens/
│   ├── dashboard1.png
│   ├── dashboard2.png
│   ├── dashboard3.png
│   ├── dashboard4.png
│   ├── grafico_sensores.png
│   ├── machine_learning1.png
│   ├── machine_learning2.png
│   ├── postgresql.png
│   └── visao_computacional.png
├── src/
│   ├── dashboard.py
│   ├── gerar_alertas.py
│   ├── gerar_dados.py
│   ├── graficos.py
│   ├── salvar_banco.py
│   └── treinar_modelo.py
├── visao_computacional/
│   ├── detectar_folha.py
│   └── folha.jpg
├── requirements.txt
└── README.md