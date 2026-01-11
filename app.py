import streamlit as st
import pandas as pd
from datetime import date
data_minima = date(1900, 1, 1)
data_maxima = date(2030, 12, 31)


st.title("Cadastro de clientes")
nome = st.text_input("Digite o nome do cliente")
endereco = st.text_input("Digite o endereço")
numero_casa = st.number_input("Número da residência", min_value=0, step=1)
telefone = st.text_input("Digite o telefone (com DDD)")
dt_nasc = st.date_input(
    "Escolha a data de nascimento",
    value=date(2000, 1, 1), # Data que aparece selecionada primeiro
    min_value=data_minima,   # Limite para o passado
    max_value=data_maxima    # Limite para o futuro
)
tipo_cliente = st.selectbox("Tipo de cliente",
                        {"Pessoa física", "Pessoa juridica"} )
cadastrar = st.button("Cadastrar Cliente")

if cadastrar:
    with open("clientes.csv", "a", encoding="utf-8")as arquivo:
            arquivo.write(f"{nome}, {endereco}, {numero_casa}, {telefone} {dt_nasc}, {tipo_cliente}.\n")
            st.success("Cliente Cadastrado com sucesso!")
#python -m streamlit run app.py