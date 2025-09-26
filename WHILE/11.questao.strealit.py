import streamlit as st

st.title("ATIVIDADE: LAÇO DE REPETIÇÃO")
st.subheader("Cadastro e Login")

tentativas = 0
login = "enzo.gostoso"
senha = "1234"

st.session_state.setdefault("desabilitar", False)
st.session_state.setdefault("tentativas", 0)

login_c = st.text_input("DIGITE SEU LOGIN: ", disabled=st.session_state.desabilitar)
senha_c = st.text_input("DIGITE SUA SENHA: ", type="password", disabled=st.session_state.desabilitar)

if st.button("VERIFICAAR"):
    if login == login_c and senha == senha_c:
        st.success("BEM VINDO!")
    else:
        st.session_state.tentativas += 1
        if st.session_state.tentativas <= 3:
            st.warning(f"LOGIN OU SENHA INÁLIDAS, tentativas: {st.session_state.tentativas}")
        else:
            st.session_state.desabilitar = True
            st.error("NUMERO DE TENTATIVAS INVÁLIDAS")
