import streamlit as st
from datetime import date

st.title("🎬 Sistema de Aluguel de Filmes e Jogos 🎮")

# Lista de produtos
produtos = [
    "Filme - O Senhor dos Anéis",
    "Filme - Matrix",
    "Jogo - FIFA 25",
    "Jogo - GTA V",
    "Filme - Interestelar"
]

# Entrada do usuário
produto_escolhido = st.selectbox("Escolha um produto para alugar:", produtos)
data_retirada = st.date_input("Data de retirada:", date.today())
data_devolucao = st.date_input("Data prevista para devolução:")

# Processamento
if st.button("Registrar Aluguel"):
    hoje = date.today()
    dias_restantes = (data_devolucao - hoje).days

    # Exibir informações
    st.write(f"📌 Produto alugado: **{produto_escolhido}**")
    st.write(f"📅 Data de retirada: {data_retirada.strftime('%d/%m/%Y')}")
    st.write(f"📅 Data de devolução: {data_devolucao.strftime('%d/%m/%Y')}")

    # Mensagens conforme prazo
    if dias_restantes > 0:
        st.success(f"⏳ Faltam {dias_restantes} dias para a devolução.")
    elif dias_restantes == 0:
        st.warning("⚠️ A devolução é HOJE!")
    else:
        st.error(f"❌ O prazo já passou há {abs(dias_restantes)} dias.")
