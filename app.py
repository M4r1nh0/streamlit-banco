import streamlit as st
import pandas as pd
import numpy as np
from requests import post
from datetime import datetime

endpoint = "https://ShockingFrostyControlflowgraph.danielmarinho.repl.co/suinox/api/v1/cadastro"

def cadastrar():
    st.title('Tela de cadastro')
    Nome = st.text_input('Digite seu nome')
    cpf = st.text_input('Digite seu cpf')
    plano = st.selectbox('Selecione um tipo de plano', ['Plano basico', 'Plano superior'])
    cidade = st.selectbox('Selecione sua cidade', ['Porto velho', 'Candeias', 'Ariquemes', 'Pimenta bueno'])
    bairro = st.text_input('Digite o bairro da sua casa')
    rua = st.text_input('Digite a rua da sua casa')
    cep = st.text_input('Digite o cep da sua casa')
    quant_porcos = st.text_input('Digite a quantidade de porcos')

    if st.button("Submit"):
        st.success('Dados enviados com sucesso')
        data = {
         "nome":Nome,
         "cpf":cpf,
         "plano":plano,
         "cidade":cidade,
         "bairro":bairro,
         "rua":rua,
         "cep":cep,
         "quant_porcos":quant_porcos,
         "datetime":str(datetime.now()),
         "carencia":0,
         "status_solicitacao":"novo_usuario",
         "Forma_pagamento":0,
         "Fatura":0,
         "Mensalidade":0
        }
        result = post(endpoint,data=data).json()
        if result == True:
            st.success("Solicitação enviada com Sucesso ")
        else:
            st.write("Ocorreu algum erro Tente novamente mais tarde ou entre em contato com nosso setor de técnico")
            st.write("email: ")
    else:
        st.info('Clique no botão enviar para enviar seus dados :)')

def Listar_user():
    st.title('Listando usuarios')
    st.write('Digite um nome do usario(cpf) ou deixe em branco')
    buscando = st.text_input('Digite um nome ou cpf')
    if st.button('Buscar'):
        data={
        "busca": buscando
        }
        #st.write(buscando)
        resultado = post("https://ShockingFrostyControlflowgraph.danielmarinho.repl.co/suinox/api/v1/lista", data=data).json()
        st.write(resultado)

def main():
    menu = st.sidebar.selectbox(
    "Menu principal",
    ("Cadastro de usuario", "Lista usuario", "Atualizar dados de usuario ","Deletar usuario")
    )
    if menu == "Cadastro de usuario":
        cadastrar()
    if menu == "Lista usuario":
        Listar_user()

if __name__ == '__main__':
    main()
