import streamlit as st

# st.title("ATIVIDADE, LAÇO DE REPETIÇÃO: WHILE")
# st.subheader("Cadastro e Login")

# login = st.text_input("CADASTRE UM LOGIN: ")
# senha = st.text_input("CADASTRE UMA SENHA: ")

# opcao = st.number_input("DESEJA FAZER LOGIN? (1) PARA SIM, E (2) PARA NÃO0", min_value=0, max_value=2,step=1)
# if opcao == 1:

#     l_login = st.text_input("INFORME SEU LOGIN:")
#     l_senha = st.text_input("INFORME A SENHA: ")
#     if l_login == login and l_senha == senha:
#             st.success(f"O EMAIL CADASTRADO É {l_login}")
#             st.success(f"A SENHA CASTRADA É {l_senha}")
#     else:
#             l_login = st.text_input("INFORME SEU LOGIN:")
#             l_senha = st.text_input("INFORME A SENHA: ")


login = "MARIA"
senha = "123"


login_l = st.text_input("DIGITE SEU LOGIN: ")
senha_l = st.text_input("DIGITE SUA SENHA: ",type="password")

if st.button("verificar"):
        if login_l == login and senha == senha_l:
              st.success("BEM-VINDO")
        else:
              st.warning("LOGIN OU SENHA INVÁLIDOS")