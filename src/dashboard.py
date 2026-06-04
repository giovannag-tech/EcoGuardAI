import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="EcoGuard AI",
    page_icon="🌱",
    layout="wide"
)

st.title("🌱 EcoGuard AI")
st.subheader("Sistema inteligente de monitoramento ambiental")

df = pd.read_csv("dados/dados_sensores.csv")

# Filtro por região
regioes = ["Todas"] + sorted(df["regiao"].unique().tolist())
regiao_escolhida = st.sidebar.selectbox("Filtrar por região", regioes)

if regiao_escolhida != "Todas":
    df_filtrado = df[df["regiao"] == regiao_escolhida]
else:
    df_filtrado = df

st.sidebar.info("Projeto FIAP - Fase 7")

# Métricas principais
col1, col2, col3, col4 = st.columns(4)

col1.metric("Temperatura média", f"{df_filtrado['temperatura'].mean():.1f} °C")
col2.metric("Umidade média", f"{df_filtrado['umidade'].mean():.1f} %")
col3.metric("Chuva média", f"{df_filtrado['chuva_mm'].mean():.1f} mm")
col4.metric("Nível médio do rio", f"{df_filtrado['nivel_rio'].mean():.1f} m")

st.divider()

# Alerta principal
risco_alto = df_filtrado[df_filtrado["risco_real"] == "ALTO"].shape[0]

if risco_alto > 0:
    st.error(f"🚨 Existem {risco_alto} registros com risco ALTO.")
else:
    st.success("✅ Nenhum risco alto encontrado na região selecionada.")

st.divider()

# Gráficos
col_graf1, col_graf2 = st.columns(2)

with col_graf1:
    st.subheader("Distribuição dos riscos")
    fig_risco = px.histogram(
        df_filtrado,
        x="risco_real",
        color="risco_real",
        title="Quantidade por nível de risco"
    )
    st.plotly_chart(fig_risco, use_container_width=True)

with col_graf2:
    st.subheader("Chuva x Nível do Rio")
    fig_chuva = px.scatter(
        df_filtrado,
        x="chuva_mm",
        y="nivel_rio",
        color="risco_real",
        hover_data=["regiao"],
        title="Relação entre chuva e nível do rio"
    )
    st.plotly_chart(fig_chuva, use_container_width=True)

st.divider()

col_graf3, col_graf4 = st.columns(2)

with col_graf3:
    st.subheader("Temperatura por leitura")
    fig_temp = px.line(
        df_filtrado,
        y="temperatura",
        title="Variação da temperatura"
    )
    st.plotly_chart(fig_temp, use_container_width=True)

with col_graf4:
    st.subheader("Umidade por leitura")
    fig_umidade = px.line(
        df_filtrado,
        y="umidade",
        title="Variação da umidade"
    )
    st.plotly_chart(fig_umidade, use_container_width=True)

st.divider()

st.subheader("Tabela completa dos sensores")
st.dataframe(df_filtrado, use_container_width=True)

st.success("EcoGuard AI em funcionamento.")