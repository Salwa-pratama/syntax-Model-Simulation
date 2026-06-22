import sys
import os

# 1. Mundur satu folder ke root (Syntax) biar Python bisa baca folder 'utils'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


import streamlit as st
import pandas as pd
from utils.run_simulation import run_simulation
from components.text import text
import numpy as np
import pickle

# Custom text untuk mempermudah styling
text('Simulasi kebijakan keuntungan toko', '#4ceb34', "50px")
st.write("Gunakan slider untuk menguji skenario 'What-if'. ")
text("Gunakan slider untuk menguji skenario 'What-if'", '#ffffff', "14px")

# Sidebar : Variabel Kontrol
st.sidebar.header("Tuas kebijakan (Intervensi)")
iklan_slider = st.sidebar.slider("Anggaran Iklan (Juta)", 0, 50, 10)
diskon_slider = st.sidebar.slider("Besaran Diskon (%)", 0, 50, 10)
# Load model and data
@st.cache_resource
def load_model():
    with open ("./models/model.pkl", "rb") as file :
        return pickle.load(file)

model = load_model()
baseline_input = np.array([[10,10]])
baseline_pred = model.predict(baseline_input)[0]
# Engine: Jalankan Simulasi
hasil_pred , delta = run_simulation(iklan_slider, diskon_slider, model, baseline_pred)


# Menampilkan hasil

col1, col2 = st.columns(2)
color = ""
keterangan = ""
if delta < 0 :
    color = "red"
    keterangan = "Nilai kurang dari baseline"
else :
    color = "green"
    keterangan = "Nilai lebih dari baseline"
col1.metric("Prediksi keuntungan", f"Rp {hasil_pred:.2f} Juta dibandingkan kondisi baseline ")
col2.write(f"Skenario ini menghasilkan perubahan sebesar :{color}[{delta:.2f}] Juta dibandingkan kondisi baseline, :{color}[{keterangan}]")

# Visualisasi perbandingan

st.title("Gambar grafik")

data_plot = pd.DataFrame({
    'Skenario' : ['Baseline', "Intervensi"],
    'Keuntungan' : [baseline_pred, hasil_pred],
    "Warna" : ['#4ceb34', '#0068c9']
})

st.bar_chart(data=data_plot, x='Skenario', y='Keuntungan', color="Warna")
