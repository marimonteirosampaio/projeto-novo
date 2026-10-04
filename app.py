
import streamlit as st

st.set_page_config(
    page_title="Valor do Dinheiro no Tempo",
    page_icon="💰"
)

st.title("💰 Valor do Dinheiro no Tempo")

st.write(
    "Aprenda matemática financeira na prática."
)

st.header("O que você vai aprender?")

st.write(
    "Juros, taxas e crescimento do dinheiro ao longo do tempo."
)

st.subheader("A fórmula dos juros compostos")

st.latex(r"M = C \times (1+i)^t")

st.write(
    "M = montante final; C = capital inicial; "
    "i = taxa de juros por período; t = número de períodos."
)
