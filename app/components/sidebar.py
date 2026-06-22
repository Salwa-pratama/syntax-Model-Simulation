import streamlit as st


def sidebar (halaman1, halaman2):

    st.sidebar.title("Menu navigasi")

    pilihan_menu = st.sidebar.radio("Halaman", {"Simulasi kebijakan 2 feature", "simulasi kebijakan 3 feature"})
    
    if pilihan_menu == "Simulasi kebijakan 2 feature":
        halaman1()
    else :
        halaman2()
