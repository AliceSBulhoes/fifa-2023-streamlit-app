import streamlit as st
import pandas as pd

def page_config():
    """Faz a configuração da página do Streamlit."""
    st.set_page_config(
        page_title="Teams Overview",
        page_icon="🏟️",
        layout="wide",
        initial_sidebar_state="expanded"
    )

page_config()

df = st.session_state.get("df_data", pd.DataFrame())

# Filtro de times
teams = st.sidebar.selectbox("Selecione um time", df["Club"].unique())
df_team = df[df["Club"] == teams].set_index("Name")

# Exibir tabela de jogadores do time selecionado
st.image(df_team["Club Logo"].iloc[0])
st.subheader(f"{teams}")

colunms = ["Age", "Photo", "Flag", "Overall", "Value(£)", "Wage(£)", "Joined", "Height(cm.)", "Weight(lbs.)", "Release Clause(£)", "Contract Valid Until"]

st.dataframe(df_team[colunms],
            column_config={
                "Overall": st.column_config.ProgressColumn("Overall", format="%d"),
                "Wage(£)": st.column_config.ProgressColumn("Wage(£)", max_value=df_team["Wage(£)"].max(), format="%d"),
                "Photo": st.column_config.ImageColumn("Photo", width="small"),
                "Flag": st.column_config.ImageColumn("Flag", width="small"),
            })