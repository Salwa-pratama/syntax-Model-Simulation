import streamlit as st
import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from components.text import text
from utils.load_model import load_model
from utils.run_simulation import run_simulation
import numpy as np
import pandas as pd

# halaman simulasi kebijakan 2 variabel
def halaman1() :
    # Custom text untuk mempermudah styling
    text('Simulasi kebijakan keuntungan toko', '#4ceb34', "50px")
    st.write("Gunakan slider untuk menguji skenario 'What-if'. ")
    text("Gunakan slider untuk menguji skenario 'What-if'", '#ffffff', "14px")

  
    iklan_slider = st.slider("Anggaran Iklan (Juta)", 0, 50, 10)
    diskon_slider = st.slider("Besaran Diskon (%)", 0, 50, 10)
    # Load model and data

    model = load_model("./models/model.pkl")
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

    text("Grafik Perbandingan", '#00ff19ff', "50px")


    data_plot = pd.DataFrame({
        'Skenario' : ['Baseline', "Intervensi"],
        'Keuntungan' : [baseline_pred, hasil_pred],
        "Warna" : ['#4ceb34', '#0068c9']
    })

    st.bar_chart(data=data_plot, x='Skenario', y='Keuntungan', color="Warna")


