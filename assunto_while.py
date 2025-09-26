import streamlit as st

st.title("LAÇO DE REPETIÇÃO - WHILE")

nota = st.number_input("DIGITE UMA NOTA: ", step=1)

if st.button("VERIFICAR"):
    if nota < 0 or nota > 10:
        st.warning("A NOTA DEVE SER ENTRE 0 E 10")
    else:
        st.info(f"NOTA: {nota}")