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

    # Definisi nilai baseline (Kondisi awal toko)
    baseline_iklan = 10
    baseline_diskon = 10

    st.markdown("### 🎛️ Variabel Kontrol (Intervensi)")
    col_slider1, col_slider2 = st.columns(2)
    with col_slider1:
        iklan_slider = st.slider("Anggaran Iklan (Juta)", 0, 50, value=baseline_iklan)
    with col_slider2:
        diskon_slider = st.slider("Besaran Diskon (%)", 0, 50, value=baseline_diskon)
    # Load model and data

    model = load_model("./models/model.pkl")
    baseline_input = np.array([[baseline_iklan, baseline_diskon]])
    baseline_pred = model.predict(baseline_input)[0]
    # Engine: Jalankan Simulasi
    hasil_pred , delta = run_simulation(iklan_slider, diskon_slider, model, baseline_pred)


    # Menampilkan hasil

    st.divider()
    st.markdown("### 📊 Ringkasan Hasil Prediksi")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(label="Kondisi Baseline", value=f"Rp {baseline_pred:.2f} Jt")
        
    with col2:
        st.metric(label="Prediksi Keuntungan (Intervensi)", value=f"Rp {hasil_pred:.2f} Jt", delta=f"{delta:.2f} Jt")
        
    with col3:
        if delta < 0:
            st.error(f"⚠️ Skenario ini menghasilkan kerugian sebesar Rp {abs(delta):.2f} Jt dari baseline.")
        elif delta > 0:
            st.success(f"✅ Skenario ini menghasilkan keuntungan ekstra sebesar Rp {delta:.2f} Jt dari baseline!")
        else:
            st.info("⚖️ Skenario ini tidak mengubah keuntungan (sama dengan baseline).")

    st.divider()
    st.markdown("### 📈 Visualisasi Perbandingan")
    data_plot = pd.DataFrame({
        'Skenario' : ['Baseline', "Intervensi"],
        'Keuntungan' : [baseline_pred, hasil_pred],
        "Warna" : ['#4ceb34', '#0068c9']
    })

    st.bar_chart(data=data_plot, x='Skenario', y='Keuntungan', color="Warna")


