import streamlit as st
import pandas as pd
import plotly.express as px

# Configurar página
st.set_page_config(page_title="Dashboard Social Media", layout="wide")

# Título
st.title("📊 Dashboard de Performance - Social Media")

# Dados
dados_ig = {
    'post': ['Post 1', 'Post 2', 'Post 3', 'Post 4', 'Post 5', 'Post 6', 'Post 7', 'Post 8'],
    'video_views': [43218, 12263, 13351, 7932, 9140, 4564, 4425, 3228],
    'engagement': [2141, 655, 452, 402, 355, 218, 139, 115]
}

dados_lk = {
    'post': ['Post 1', 'Post 2', 'Post 3', 'Post 4', 'Post 5'],
    'impressions': [10894, 8387, 6218, 5181, 4743],
    'engagement': [767, 587, 287, 268, 217]
}

df_ig = pd.DataFrame(dados_ig)
df_lk = pd.DataFrame(dados_lk)

# Cards com métricas principais
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Views IG", f"{df_ig['video_views'].sum():,}")
    
with col2:
    st.metric("Total Engagement IG", f"{df_ig['engagement'].sum():,}")
    
with col3:
    st.metric("Total Impressions LK", f"{df_lk['impressions'].sum():,}")
    
with col4:
    st.metric("Total Engagement LK", f"{df_lk['engagement'].sum():,}")

# Dividir em duas colunas
col1, col2 = st.columns(2)

with col1:
    st.subheader("📸 Instagram Performance")
    fig_ig = px.bar(df_ig, x='post', y='video_views', 
                    title='Video Views por Post',
                    color_discrete_sequence=['#E1306C'])
    st.plotly_chart(fig_ig, use_container_width=True)

with col2:
    st.subheader("💼 LinkedIn Performance")
    fig_lk = px.bar(df_lk, x='post', y='impressions',
                    title='Impressions por Post',
                    color_discrete_sequence=['#0A66C2'])
    st.plotly_chart(fig_lk, use_container_width=True)

# Tabela de dados
st.subheader("📋 Dados Completos")
tab1, tab2 = st.tabs(["Instagram", "LinkedIn"])

with tab1:
    st.dataframe(df_ig, use_container_width=True)
    
with tab2:
    st.dataframe(df_lk, use_container_width=True)
