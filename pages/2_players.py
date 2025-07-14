import streamlit as st
import pandas as pd

def page_config():
    """Faz a configuração da página do Streamlit."""
    st.set_page_config(
        page_title="Player Details",
        page_icon="⚽",
        layout="wide",
        initial_sidebar_state="expanded"
    )

page_config()

df = st.session_state.get("df_data", pd.DataFrame())

# Filtro Clube
clubes = st.sidebar.selectbox("Selecione um clube", df["Club"].unique())
df_club = df[df["Club"] == clubes]

# Filtro jogadores
player = st.sidebar.selectbox("Selecione um jogador", df_club["Name"].unique())

# Página de detalhes do jogador
df_player = df_club[df_club["Name"] == player].iloc[0]

st.image(df_player["Photo"])
st.title(df_player["Name"])
st.markdown(f"**Clube:** {df_player['Club']}")
st.markdown(f"**Posição:** {df_player['Position']}")

# Colunas para exibir informações do jogador
col1, col2, col3, col4 = st.columns(4)
col1.markdown(f"**Idade:** {df_player['Age']}")
col2.markdown(f"**Altura:** {df_player['Height(cm.)'] / 100} cm")
col3.markdown(f"**Peso:** {df_player['Weight(lbs.)'] * 0.453:.2f}")
# Linha
st.divider()
# pontuação do jogador
st.subheader(f"Overall {df_player['Overall']}")
# Barra de progresso
st.progress(int(df_player["Overall"]))

# Colunas para metricas do jogador
col1, col2, col3, col4 = st.columns(4)
col1.metric(label="Valor de Mercado", value=f"£{df_player['Value(£)']:,}")
col2.metric(label="Salário", value=f"£{df_player['Wage(£)']:,}")
col3.metric(label="Clásula de Rescisão", value=f"£{df_player['Release Clause(£)']:,}")  

