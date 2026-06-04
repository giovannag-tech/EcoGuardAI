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

```---

# 📊 Dashboard Interativo

### Visão Geral do Sistema

![Dashboard Principal](imagens/dashboard1.png)

**Função:** Tela principal do EcoGuard AI.

**O que mostra:** indicadores ambientais, temperatura, umidade, chuva, nível do rio e alertas automáticos de risco.

---

### Distribuição dos Riscos

![Dashboard Riscos](imagens/dashboard2.png)

**Função:** Exibir a classificação dos riscos ambientais.

**O que mostra:** quantidade de registros classificados como Baixo, Médio e Alto risco pelo modelo de Machine Learning.

---

### Análise Climática

![Dashboard Clima](imagens/dashboard3.png)

**Função:** Monitoramento das condições ambientais.

**O que mostra:** gráficos de temperatura, umidade, chuva e comportamento dos sensores.

---

### Monitoramento Ambiental

![Dashboard Sensores](imagens/dashboard4.png)

**Função:** Apoiar a tomada de decisão.

**O que mostra:** evolução dos dados ambientais utilizados pelo sistema.

---

# 📈 Análise dos Sensores

![Gráfico Sensores](imagens/grafico_sensores.png)

**Função:** Visualizar tendências ambientais.

**O que mostra:** comportamento dos sensores ao longo do tempo para identificar situações críticas.

---

# 🤖 Machine Learning

![Treinamento do Modelo](imagens/machine_learning1.png)

**Função:** Treinamento do modelo preditivo.

**O que mostra:** algoritmo de Machine Learning responsável pela classificação automática dos riscos ambientais.

---

![Resultado da Previsão](imagens/machine_learning2.png)

**Função:** Teste do modelo treinado.

**O que mostra:** previsão automática de risco (Alto, Médio ou Baixo) baseada nos dados recebidos.

---

# 🗄️ Banco de Dados PostgreSQL

![Banco PostgreSQL](imagens/postgresql.png)

**Função:** Armazenamento dos dados ambientais.

**O que mostra:** tabela contendo as leituras dos sensores utilizadas pelo sistema.

---

# 👁️ Visão Computacional

![Visão Computacional](imagens/visao_computacional.png)

**Função:** Análise visual de folhas.

**O que mostra:** utilização do OpenCV para processamento de imagens agrícolas.

---

# ⚠️ Sistema de Alertas

O sistema gera alertas automáticos para:

- Enchentes
- Deslizamentos
- Queimadas

Os alertas são exibidos diretamente no Dashboard para auxiliar a tomada de decisão preventiva.

---

# 👩‍💻 Desenvolvido por

**Giovanna Gomes Oliveira**

Projeto desenvolvido para aplicação dos conceitos estudados no curso de Inteligência Artificial da FIAP.text
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