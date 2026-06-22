import streamlit as st

# Konfigurasi halaman dasar (wajib dipanggil pertama kali)
st.set_page_config(
    page_title="Dashboard Simulasi Kebijakan",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

from components.sidebar import sidebar
from views.halaman1 import halaman1
from views.halaman2 import halaman2

sidebar(halaman1, halaman2)
