
import streamlit as st

st.set_page_config(
    page_title="Valor do Dinheiro no Tempo",
    page_icon="💰",
    layout="wide"
)

st.title("💰 Finanças na Prática")
st.subheader("Valor do Dinheiro no Tempo")

st.write(
    "Descubra como o tempo, os juros e as decisões financeiras "
    "influenciam o valor do dinheiro."
)

conceito, simulador, desafio, referencias = st.tabs([
    "Conceito",
    "Simulador",
    "Desafio",
    "Referências"
])

with conceito:
    st.header("O que é o valor do dinheiro no tempo?")
    st.write(
        "Uma quantia disponível hoje pode ser investida e gerar "
        "rendimentos ao longo do tempo."
    )
    st.subheader("A fórmula dos juros compostos")
    st.latex(r"M = C \times (1+i)^t")
    st.write("M = montante; C = capital; i = taxa por período; t = prazo.")

with simulador:
    st.header("Simule seu investimento")
    capital = st.number_input(
        "Valor inicial (R$)", min_value=0.01,
        value=1000.0, step=100.0
    )
    taxa = st.number_input(
        "Taxa mensal (%)", min_value=0.0,
        max_value=100.0, value=1.0, step=0.5
    )
    tempo = st.number_input(
        "Prazo em meses", min_value=1,
        max_value=600, value=12, step=1
    )

    if st.button("Calcular montante"):
        montante = capital * (1 + taxa / 100) ** tempo
        juros = montante - capital
        st.metric("Montante final", f"R$ {montante:,.2f}")
        st.metric("Juros acumulados", f"R$ {juros:,.2f}")

        historico = [
            capital * (1 + taxa / 100) ** mes
            for mes in range(tempo + 1)
        ]
        st.line_chart(historico)

with desafio:
    st.header("Desafio rápido")
    st.write("R$ 1.000 aplicados a 1% ao mês terão qual saldo após um mês?")
    resposta = st.radio(
        "Escolha uma alternativa:",
        ["R$ 1.000,00", "R$ 1.010,00", "R$ 1.100,00"],
        index=None
    )

    if st.button("Conferir resposta"):
        if resposta == "R$ 1.010,00":
            st.success("Correto! R$ 1.000 × 1,01 = R$ 1.010,00.")
        elif resposta is None:
            st.warning("Selecione uma alternativa.")
        else:
            st.error("Não é essa. Tente novamente.")

with referencias:
    st.header("Referência bibliográfica")
    st.write(
        "BERK, J.; DEMARZO, P.; HARFORD, J. "
        "Fundamentos de finanças empresariais. "
        "Porto Alegre: Bookman, 2010."
    )
    st.info(
        "Simulação educativa, sem impostos, tarifas ou variações reais "
        "de rentabilidade."
    )

st.divider()
st.caption("Projeto educacional de Matemática Financeira · UFMG")
