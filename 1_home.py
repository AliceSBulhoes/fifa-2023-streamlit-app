import streamlit as st
import pandas as pd
import webbrowser

def page_config():
    """Faz a configuração da página do Streamlit."""
    st.set_page_config(
        page_title="FIFA World Cup",
        page_icon="🏆",
        layout="wide",
        initial_sidebar_state="expanded"
    )

@st.cache_data
def load_data():
    """
    Carrega os dados do CSV e armazena no session state.
    Recomenda-se usar @st.cache_data para otimizar o carregamento de dados.
    """
    if "data" not in st.session_state:
        df = pd.read_csv("./data/CLEAN_FIFA23_official_data.csv")
        df = df[df['Contract Valid Until'] >= 2023]
        df = df[df["Value(£)"] > 0]
        df = df.sort_values(by="Overall", ascending=False)
        st.session_state["df_data"] = df
    return st.session_state["df_data"]

page_config()
df = load_data()

st.markdown("""# Fifa World Cup 2023 Dataset! :soccer:""")
st.sidebar.markdown("Desenvolvido por [Alice](https://github.com/AliceSBulhoes)")

# Botão para acessar os dados do Kaggle
btn = st.link_button("Acesse os dados do Kaggle", "https://www.kaggle.com/datasets/kevwesophia/fifa23-official-datasetclean-data")

st.markdown("""
    O conjunto de dados de jogadores de futebol de 2017 a 2023 fornece informações abrangentes sobre jogadores de futebol profissionais. O conjunto de dados contém uma ampla gama de atributos, incluindo dados demográficos dos jogadores, características físicas, estatísticas de jogo, detalhes de contratos e afiliações de clubes. Com mais de 17.000 registos, este conjunto de dados oferece um recurso valioso para analistas de futebol, investigadores e entusiastas interessados em explorar vários aspectos do mundo do futebol, pois permite estudar atributos de jogadores, métricas de desempenho, avaliação de mercado, análise de clubes, posicionamento de jogadores e desenvolvimento de jogadores ao longo do tempo.
""")